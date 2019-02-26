from rply import ParserGenerator
from rply.token import BaseBox
from myTypes import Boolean, Integer, Double, Array, create, Pointer

Memory = {}

def init(ident, _type):
    if Memory.get(ident.value, False):
        # raise Exception(f'ID {ident} already defined')
        print(f'ID {ident} already defined')
    Memory[ident.value] = _type

def get_type(ident):
    if ident.gettokentype() == 'ID':
        data = Memory.get(ident.value, False)
        if data:
            dtype = data.gettokentype()
            # if ident Type is array -> get type of its elements
            if dtype == 'ARRAY':
                return data._type
            # else ident just return type
            return dtype
        # raise Exception(f'ID {ident} not initialized!')
        print(f'ID {ident} not initialized!')
    else:
        return ident.gettokentype()


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['OPEN_PAREN', 'CLOSE_PAREN', 'ID',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'PROGRAM',
             'BEGIN', 'END', 'ASSIGNMENT', 'COLON', 'FTYPE',
             'ITYPE', 'COMMA', 'LESS', 'MORE', 'AND', 'OR', 'VAR',
             'ARRAY', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'RANGE', 'OF', 'IF',
             'ELSE', 'FOR', 'DO', 'THEN', 'TO', 'EQUAL', 'NEQUAL', 'FUNCTION',
             'BTYPE', 'BOOLEAN', 'POINTER']
        )

    def parse(self):

        # PROGRAM DECLARATION SECTION

        @self.pg.production('program : PROGRAM ID SEMI_COLON DeclarationSection Block')
        def program(p):
            pass

        @self.pg.production('DeclarationSection : ')
        @self.pg.production('DeclarationSection : DeclarationSection WhichSection')
        def DeclarationSection(p):
            pass

        # parse which section is used
        @self.pg.production('WhichSection : TypeSection')
        @self.pg.production('WhichSection : FuncSection')
        def WhichSection(p):
            pass

        @self.pg.production('TypeSection : VAR ColonTypeDeclaration')
        def TypeSection(p):
            pass

        @self.pg.production('ColonTypeDeclaration : ColonTypeDeclaration TypeDeclaration SEMI_COLON')
        @self.pg.production('ColonTypeDeclaration : TypeDeclaration SEMI_COLON')
        def ColonTypeDeclaration(p):
            pass

        @self.pg.production('TypeDeclaration : IDList COLON Type')
        def TypeDeclaration(p):
            # fill Memory with id types
            if not isinstance(p[0], list):
                if not p[0]._ispointer:
                    init(p[0], p[2])
                else:
                    init(p[0], Pointer(p[0], p[2]))
            else:
                for token in p[0]:
                    if not token._ispointer:
                        init(token, p[2])
                    else:
                        init(token, Pointer(token, p[2]))

        @self.pg.production('IDList : IdType COMMA IDList')
        @self.pg.production('IDList : IdType')
        def IDList(p):
            # return identifiers list
            if len(p) == 1:
                return p[0]
            else:
                if not isinstance(p[2], list):
                    return [p[2], p[0]]
                return p[2] + [p[0]]

        @self.pg.production('IdType : ID')
        @self.pg.production('IdType : POINTER ID')
        def IdType(p):
            if len(p) == 1:
                p[0]._ispointer = False
                return p[0]
            else:
                p[1]._ispointer = True
                return p[1]

        @self.pg.production('Type : ITYPE')
        @self.pg.production('Type : FTYPE')
        @self.pg.production('Type : ArrayType')
        @self.pg.production('Type : BTYPE')
        def Type(p):
            # return type itself
            return p[0]

        @self.pg.production('ArrayType : ARRAY OPEN_BRACKET ITYPE RANGE ITYPE CLOSE_BRACKET OF Type')
        def ArrayType(p):
            # return array + values `type`
            p[0].value += f' {p[-1].value}'
            p[0]._type = p[-1]
            return p[0]

        @self.pg.production('FuncSection : FuncHeading SEMI_COLON DeclarationSection Block')
        def FuncSection(p):
            pass

        @self.pg.production('FuncHeading : FUNCTION ID OPEN_PAREN ParamList CLOSE_PAREN COLON Type')
        def FuncHeading(p):
            pass

        @self.pg.production('ParamList : IDList COLON Type SEMI_COLON ParamList')
        @self.pg.production('ParamList : IDList COLON Type')
        @self.pg.production('ParamList : ')
        def ParamList(p):
            pass

        # BEGIN ... END - BLOCK

        @self.pg.production('Block : BEGIN END SEMI_COLON')
        @self.pg.production('Block : BEGIN StatementList END SEMI_COLON')
        def Block(p):
            pass

        @self.pg.production('StatementList : Statement StatementList')
        @self.pg.production('StatementList : Statement')
        def StatementList(p):
            pass

        @self.pg.production('Statement : SimpleStatement SEMI_COLON')
        @self.pg.production('Statement : IfStatement')
        @self.pg.production('Statement : LoopStatement')
        def Statement(p):
            pass

        # IF - ELSE IF - ELSE

        @self.pg.production('IfStatement : IF expression THEN StatementList Else')
        def IfStatement(p):
            pass

        @self.pg.production('Else : ')
        @self.pg.production('Else : ELSE IfStatement')
        @self.pg.production('Else : ELSE StatementList')
        def Else(p):
            pass

        @self.pg.production('SimpleStatement : expression')
        @self.pg.production('SimpleStatement : assignment')
        def SimpleStatement(p):
            pass

        # LOOPS
        @self.pg.production('LoopStatement : FOR ID ASSIGNMENT ITYPE TO ITYPE DO Block')
        @self.pg.production('LoopStatement : FOR ID ASSIGNMENT ITYPE TO ITYPE DO Statement')
        def LoopStatement(p):
            pass

        # ASSIGNMENT
        @self.pg.production('assignment : ID ASSIGNMENT expression')
        @self.pg.production('assignment : ID OPEN_BRACKET ITYPE CLOSE_BRACKET ASSIGNMENT expression')
        @self.pg.production('assignment : ID OPEN_BRACKET ID CLOSE_BRACKET ASSIGNMENT expression')
        def assignment(p):
            if len(p) == 3:
                ltype = get_type(p[0])
                rtype = get_type(p[-1])
                if ltype != rtype:
                    print(f"Can't assign {rtype} to {ltype}")
            elif len(p) == 6:
                ltype = get_type(p[0]).gettokentype()
                rtype = get_type(p[-1])
                if ltype != rtype:
                    print(f"Can't assign {rtype} to {ltype}")

        # ARIPHMETICS AND LOGIC EXPRESSION
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : expression MORE expression')
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression OR expression')
        @self.pg.production('expression : expression EQUAL expression')
        @self.pg.production('expression : expression NEQUAL expression')
        def expression(p):
            operator = p[1]
            left = p[0]
            right = p[2]

            # get operand type
            ltype = get_type(left)
            rtype = get_type(right)

            # only BOOLEAN can be used
            if operator.gettokentype() in ['AND', 'OR']:
                if ltype != 'BTYPE' or rtype != 'BTYPE':
                    # raise Exception(
                        # f'Incorrect types for boolean ariphmetic {p[0].value} ({ltype}) {p[1].gettokentype()} {p[2].value} ({rtype}) at {p[1].getsourcepos()}')
                    print(
                        f'Incorrect types for boolean ariphmetic {p[0].value} ({ltype}) {p[1].gettokentype()} {p[2].value} ({rtype}) at {p[1].getsourcepos()}')
                return Boolean()

            # do not support silent type swapping
            if ltype != rtype:
                # raise Exception(
                    # f"Can't {p[1].gettokentype()} {rtype} on {ltype}")
                print(f"Can't {p[1].gettokentype()} {rtype} on {ltype}")

            # <, >, <>, == -> Boolean
            if operator.gettokentype() in ['LESS', 'MORE', 'EQUAL', 'NEQUAL']:
                return Boolean()

            return create(ltype)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def paren_expression(p):
            return p[1]

        @self.pg.production('expression : ID OPEN_PAREN IDList CLOSE_PAREN')
        @self.pg.production('expression : ID OPEN_PAREN CLOSE_PAREN')
        def function_expression(p):
            pass

        @self.pg.production('expression : ID OPEN_BRACKET ITYPE CLOSE_BRACKET')
        @self.pg.production('expression : ID OPEN_BRACKET ID CLOSE_BRACKET')
        def bracket_expression(p):
            if p[0].gettokentype() == "ID":
                _type = Memory[p[0].value]
                if _type.gettokentype() != 'ITYPE' :
                    print(f"Cant't use {_type.value} as index")

            # get array type
            return get_type(p[0])

        @self.pg.production('expression : ITYPE')
        @self.pg.production('expression : FTYPE')
        @self.pg.production('expression : ID')
        @self.pg.production('expression : BOOLEAN')
        def number(p):
            # if ident not in var/const/type section
            # aka not in declaration section
            # check if it was initialized
            if p[0].gettokentype() == 'ID':
                get_type(p[0])
            # return ITYPE or FLOAT etc
            return p[0]

        @self.pg.error
        def error_handle(token):
            raise Exception(f'{token.value}, {token.getsourcepos()}')

    def get_parser(self):
        return self.pg.build()
