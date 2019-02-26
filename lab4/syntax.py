from pascal import *

# while (n>0 and b=a[n]) do n:=n-1
# if c<>0 then b:=d else b:=2*a[n];
# b:= d; b:=2*a[n];


syntax = {
    "START_STATE":  {EOF: "END_STATE", IDENT: "START_ASSIGN", WHILE: "KEYWORD", IF: "KEYWORD", FOR: "KEYWORD", DO: "KEYWORD", THEN: "KEYWORD", ELSE: "KEYWORD"},
    "START_ASSIGN": {ASSIGN: "READ_EXPR"},
    "READ_EXPR":    {IDENT: "READ_OPR", INT: "READ_OPR", FLOAT: "READ_OPR", LPAREN: "READ_EXPR"},
    "READ_OPR":     {SEMICOLON: "START_STATE", PLUS: "READ_EXPR", MINUS: "READ_EXPR", ASTERISK: "READ_EXPR", AND: "READ_EXPR", GT: "READ_EXPR", EQ: "READ_EXPR",
                     NOTEQ: "READ_EXPR",  LBRACE: "READ_BRACE", RPAREN: "READ_OPR", LPAREN: "FUNCTION", ASSIGN: "READ_EXPR",  DO: "KEYWORD", THEN: "KEYWORD", ELSE: "KEYWORD"},
    "READ_BRACE":   {IDENT: "READ_BRACEEXPR", INT: "READ_BRACEEXPR"},
    "READ_BRACEEXPR": {RBRACE: "READ_OPR", PLUS: "READ_BRACE", MINUS: "READ_BRACE"},
    "KEYWORD":      {LPAREN: "READ_EXPR", IDENT: "READ_OPR"},
    "FUNCTION":      {IDENT: "READ_OPR", INT: "READ_OPR", FLOAT: "READ_OPR"}
}


def syntax_analysis(token_input):
    tokens = token_input + [("EOF", "EOF")]
    state = "START_STATE"
    count_paren = 0
    count_brace = 0
    for token in tokens:
        if token[1] in syntax[state].keys():
            #print(state, "->", syntax[state][token[1]], ", with", token[1])
            state = syntax[state][token[1]]
            if token[1] == LPAREN:
                count_paren += 1
            elif token[1] == RPAREN:
                count_paren -= 1
            if token[1] == LBRACE:
                count_paren += 1
            elif token[1] == RBRACE:
                count_paren -= 1
        else:
            if token[0] == 'EOF':
                if count_paren != 0:
                    print("Syntax error: paren exception")
                    return
                if count_brace != 0:
                    print("Syntax error: paren exception")
                    return
                print("Syntax error: no semicolomn")
                return
            print("Syntax error: state", state,
                  "with unexpected token", token)
            return
    if count_paren != 0:
        print("Syntax error: paren exception")
        return
    if count_brace != 0:
        print("Syntax error: paren exception")
        return
    print("The statement is correct")
