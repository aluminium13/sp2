from pascal import *

syntax = {
    "START_STATE":  {EOF: "END_STATE", IDENT: "START_ASSIGN", "KEYWORD": "KEYWORD"},
    "START_ASSIGN": {ASSIGN: "READ_EXPR"},
    "READ_EXPR":    {IDENT: "READ_OPR", INT: "READ_OPR", FLOAT: "READ_OPR", LPAREN: "READ_EXPR"},
    "READ_OPR":     {SEMICOLON: "START_STATE", "OPERATOR": "READ_EXPR", LBRACE: "READ_BRACE", RPAREN: "READ_OPR", LPAREN: "FUNCTION", ASSIGN: "READ_EXPR",  "KEYWORD": "KEYWORD"},
    "READ_BRACE":   {IDENT: "READ_BRACEEXPR", INT: "READ_BRACEEXPR"},
    "READ_BRACEEXPR": {RBRACE: "READ_OPR", PLUS: "READ_BRACE", MINUS: "READ_BRACE"},
    "KEYWORD":      {LPAREN: "READ_EXPR", IDENT: "READ_OPR", "KEYWORD": "KEYWORD", SEMICOLON: "START_STATE"},
    "FUNCTION":      {IDENT: "READ_OPR", INT: "READ_OPR", FLOAT: "READ_OPR"}
}


def syntax_analysis(token_input, characters):
    tokens = token_input + [("EOF", "EOF")]
    state = "START_STATE"
    count_paren, count_brace, index = 0, 0, 0
    for token in tokens:
        if token[1] in Keywords and "KEYWORD" in syntax[state].keys():
            #print(state, "->", syntax[state]["KEYWORD"], ", with", token[1])
            if tokens[index][1] ==  ELSE and tokens[index-1][1] == SEMICOLON:
                lenTokens = sum(len(char) for char, _ in tokens[:index])
                ind = characters[lenTokens:].index(token[0]) + lenTokens + characters[:lenTokens].count(" ") - 1
                print("Syntax error: Statement state %s at %i with unexpected token %s (toke index: %i)" % (state, ind, token, index))
                return
            state = syntax[state]["KEYWORD"]
        elif token[1] in Operators and "OPERATOR" in syntax[state].keys():
            if tokens[index-2][1] == BEGIN and token[1] != ASSIGN:
                lenTokens = sum(len(char) for char, _ in tokens[:index])
                ind = characters[lenTokens:].index(token[0]) + lenTokens + characters[:lenTokens].count(" ") - 1
                print("Syntax error: Statement state %s at %i with unexpected token %s (toke index: %i)" % (state, ind, token, index))
                return
            #print(state, "->", syntax[state]["OPERATOR"], ", with", token[1])
            state = syntax[state]["OPERATOR"]
        elif token[1] in syntax[state].keys():
            #print(state, "->", syntax[state][token[1]], ", with", token[1])
            state = syntax[state][token[1]]
            if token[1] == LPAREN:
                count_paren += 1
            elif token[1] == RPAREN:
                if count_paren == 0:
                    lenTokens = sum(len(char) for char, _ in tokens[:index])
                    ind = characters[lenTokens:].index(")") + lenTokens + characters[:lenTokens].count(" ") - 1
                    print("Syntax error: paren exception at", ind)
                    return
                count_paren -= 1
            if token[1] == LBRACE:
                count_paren += 1
            elif token[1] == RBRACE:
                if count_brace == 0:
                    lenTokens = sum(len(char) for char, _ in tokens[:index])
                    ind = characters[lenTokens:].index("]") + lenTokens + characters[:lenTokens].count(" ") - 1
                    print("Syntax error: brace exception at", ind)
                    return
                count_paren -= 1
        else:
            if token[0] == 'EOF':
                if ParenBraceCheck(count_paren, count_brace, characters):
                    return
                print("Syntax error: no semicolomn at", len(characters))
                return
            #ind =  characters.index(token[0])
            lenTokens = sum(len(char) for char, _ in tokens[:index])
            ind = characters[lenTokens:].index(
                token[0]) + lenTokens + characters[:lenTokens].count(" ") - 1
            print("Syntax error: Statement state %s at %i with unexpected token %s (toke index: %i)" % (
                state, ind, token, index))
            return
        index += 1
    if ParenBraceCheck(count_paren, count_brace, characters):
        return
    print("The statement is correct")


def ParenBraceCheck(count_paren, count_brace, characters):
    if count_paren != 0:
        if count_paren <= 0:
            ind = len(characters) - characters[::-1].index(")")
        if count_paren >= 0:
            ind = len(characters) - characters[::-1].index("(")
        print("Syntax error: paren exception at", ind)
        return True
    if count_brace != 0:
        if count_brace <= 0:
            ind = len(characters) - characters[::-1].index("]")
        if count_brace >= 0:
            ind = len(characters) - characters[::-1].index("[")
        print("Syntax error: brace exception at", ind)
        return True
    return False
