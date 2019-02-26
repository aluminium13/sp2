from pascal import *
from pprint import pprint
from pascal import pascal_lex

# def print(*args, **kwargs):
#     pass

counter = 0
Context = {}
assembly = ""


def initialize(ident, type):
    if ident.find("[") != -1 and ident.find("]") != -1:
        Context[ident.split("[")[0]] = type + " array"
        return
    if Context.get(ident, False):
        raise Exception('variable already declared '+ident)
    Context[ident] = type


def gtype(ident):
    if ident.find("[") != -1 and ident.find("]") != -1:
        _type = Context.get(ident.split("[")[0])
    else:
        _type = Context.get(ident, False)
    if _type:
        return _type
    raise Exception('Not initialized variable '+ident)


class syntax_node(object):
    def __init__(self, name, cont=None):
        self.name = name
        self._children = []
        self.cont = cont

    def add_child(self, child):
        self._children.append(child)

    def __repr__(self):
        return self.name + '\t' + ' '.join([str(child) for child in self._children])


class tokens_container(object):
    def __init__(self, tokens, real_tokens):
        self.tokens = tokens
        self.real_tokens = real_tokens
        self.i = 0

    def expect(self, token, fnname=""):
        keywords = [AND, WHILE, DO, ELSE, FOR, IF, THEN, LBRACKET, RBRACKET, LONG_TYPE,
                    END, VOID, INT_TYPE, DOUBLE_TYPE, BEGIN, 'END', AND, OR, BOOL_TYPE, FUNCTION]
        if token == "IDENT":
            if self.real_tokens[self.i][0] not in keywords:
                self.i += 1
                return self.tokens[self.i-1]
            else:
                print("error occured @"+fnname)
                print("syntax error at token @"+str(self.i))
                print("ident name cannot be reserved #"+token)
                exit(0)
        if self.tokens[self.i] != token:
            print("error occured @"+fnname)
            print("syntax error with unexpected token:",
                  self.real_tokens[self.i], '@'+str(self.i))
            print("expected #"+token)
            exit(0)
        self.i += 1
        return self.tokens[self.i-1]

    def maybe(self, token):
        if self.i >= len(self.tokens):
            return False

        if isinstance(token, list):
            if self.tokens[self.i] in token:
                self.i += 1
                return True
        if self.tokens[self.i] == token:
            self.i += 1
            return True
        return False


from shunting import *


def parse_expr(tokens, real_tokens):

    inp = ' '.join(i[0] for i in real_tokens)
    _count_br = 0
    for i in inp:
        if i == "(":
            _count_br += 1
        if i == ")":
            _count_br -= 1
            if _count_br < 0:
                print("@parse_expr: shunting syntax error")
                print("for input:", inp)
                exit(1)
    if _count_br != 0:
        print("@parse_expr: shunting syntax error")
        print("for input:", inp)
        exit(1)
    operators = ['-', '+', '*', '/']

    for i in range(len(inp)):
        if inp[i] in operators and inp[i+1] in operators:
            print("@parse_expr: shunting syntax error")
            print("for input:", inp)
            exit(1)
        if len(inp) > (i + 1):
            if inp[i] in [")", "("] and inp[i+1] in operators:
                print("@parse_expr: shunting syntax error")
                print("for input:", inp)
                exit(1)

    try:
        res = shunting(get_input(inp))
    except IndexError:
        print("@parse_expr: shunting syntax error")
        print("for input:", inp)
        exit(1)
    if res[-1][2] is not None:
        res = res[-1][2]
    else:
        res = res[-2][2]
    inp = res.split()
    cur_node = syntax_node(inp[0])
    try:
        stack = []
        operators = ['-', '+', '*', '/']
        for i in inp:
            if i not in operators:
                stack.append(syntax_node(i))
            else:
                new_node = syntax_node(i)
                new_node.add_child(stack.pop())
                new_node.add_child(stack.pop())
                stack.append(new_node)
        stack[-1].cont = inp
        return stack[-1]
    except IndexError:
        print("@parse_expr: shunting syntax error")
        print("for input:", ''.join(i[0] for i in real_tokens))
        exit(1)


def parse_stmnt(tokens, real_tokens):
    temp_token = syntax_node("statement_node")
    if True:
        temp_token = syntax_node(real_tokens[tokens.i-1][0])
        _type = real_tokens[tokens.i - 1][0]
        if tokens.maybe("*"):
            tokens.expect(IDENT)
            initialize(real_tokens[tokens.i - 1][0], 'pointer to ' + _type)
            new_token = syntax_node("pointer")
            new_token.add_child(syntax_node(real_tokens[tokens.i][0]))
            temp_token.add_child(new_token)
        else:
            tokens.expect(IDENT)
            # if we found array
            if tokens.maybe('['):
                new_token = syntax_node("array")
                if tokens.maybe(['IDENT', 'int']):
                    initialize(real_tokens[tokens.i - 3]
                               [0], 'array of ' + _type)
                    expr = parse_expr(tokens, real_tokens[tokens.i - 1][0])
                    new_token.add_child(expr)
                tokens.expect(']')
                temp_token.add_child(new_token)
            else:
                temp_token.add_child(syntax_node(real_tokens[tokens.i-1][0]))
                initialize(real_tokens[tokens.i - 1][0], _type)
        while tokens.maybe(','):
            if tokens.maybe("*"):
                tokens.expect(IDENT)
                initialize(real_tokens[tokens.i - 1][0], 'pointer to ' + _type)
                new_token = syntax_node("pointer")
                new_token.add_child(syntax_node(real_tokens[tokens.i-1][0]))
                temp_token.add_child(new_token)
            else:
                tokens.expect(IDENT)
                initialize(real_tokens[tokens.i - 1][0], _type)
                temp_token.add_child(syntax_node(real_tokens[tokens.i-1][0]))
        tokens.expect(';')
    return temp_token


def parse_e(tokens, real_tokens):
    fnname = 'parse_e'
    # print(tokens.tokens)
    if tokens.maybe(["DOUBLE_TYPE", "INT_TYPE", "BOOL_TYPE"]):
        return parse_stmnt(tokens, real_tokens)
    if tokens.maybe(['function']):
        return syntax_node(real_tokens[tokens.i][0])
    if tokens.maybe(['print']):
        tokens.expect('(')
        tokens.expect('IDENT')
        new_node = syntax_node('print')
        new_node.add_child(syntax_node(real_tokens[tokens.i-1][0]))
        tokens.expect(')')
        return new_node

    tokens.expect(IDENT, fnname=fnname)
    new_node = syntax_node(real_tokens[tokens.i-1][0])
    temp_node = syntax_node(":=")
    # get ident type
    _type = gtype(real_tokens[tokens.i - 1][0])
    temp_node.add_child(new_node)
    tokens.expect(":=", fnname=fnname)
    # parse expression node
    expr = parse_expr(tokens, real_tokens[tokens.i:-1])
    if not type_check(expr, Context, _type):
        print("@parse_e: type error")
        exit(1)
    temp_node.add_child(expr)
    tokens.i = len(tokens.tokens) - 1
    tokens.expect(";")
    return temp_node


def semantic_analysis(token_test, real_tokens):
    if_node = parse_e(tokens_container(
        token_test, real_tokens), real_tokens)
    return if_node


def type_check(node, types, _type: str):
    if "array" in _type:
        _type = _type.split()[0]
    if "[" in node.name:
        return True
    if node.name == 'print':
        return True
    if node.name == 'function':
        return False
    if node.name in ['+', '-', '*', '/'] and _type == 'double':
        for i in node._children:
            if type_check(i, types, _type) == False:
                return False
        return True
    if node.name in ['+', '-', '*', '/'] and (_type == 'int' or _type == 'int array'):
        for i in node._children:
            if type_check(i, types, _type) == False:
                return False
        return True
    if node.name in ['and', 'or', '=', '!='] and _type == 'bool':
        for i in node._children:
            if type_check(i, types, _type) == False:
                return False
        return True
    if node.name in types.keys():
        return types[node.name] == _type
    # can be int or float (2, 3.33)
    other = pascal_lex(node.name)[0][1]
    if other == _type:
        return True
    return False


def print_graph(node, pref=0):
    # print('-'*pref + '-->' + node.name)
    for i in node._children:
        print_graph(i, pref+1)


characters = """
int b, a[4], n;
n := 3;
a[2] := n;
a[3] := a[2]; 
b := a[3];
"""


# COMPILING

all_tokens = pascal_lex(characters)

for tok in all_tokens:
    print(tok)

tokens = []
opened = 0

from test import *
head = """
#include <stdio.h>\n
int main(void){
"""
assembly = "\t__asm\n\t{\n"
tail = """
\tprintf("n=%d\\n", n);
\tgetchar();
}
"""
asm_end = "\t}\n"

for i in all_tokens:
    if i[0] != ';':
        tokens.append(i)
        opened = 1
        continue
    tokens.append(i)
    root_node = semantic_analysis([tok[1] for tok in tokens], tokens)
    # print_graph(root_node)
    assembly += compile(root_node)[0]
    head+=compile(root_node)[1] 
    tail = compile(root_node)[2] + tail 
    tokens = []
    opened = 0

if opened != 0:
    print("error @all\nunexpected EOF")

with open('test.c', 'w+') as f:
    f.write(head+assembly+asm_end+tail)
