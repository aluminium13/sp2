import sys
import re


def lex(characters, token_exprs):
    pos = 0
    tokens = []
    characters = characters.lower()
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            token = (characters[pos], "ILLEGAL")
            tokens.append(token)
            return tokens
        else:
            pos = match.end(0)

    return tokens


def hasNoErrors(tokens, characters):
    for i in range(len(tokens)):
        if tokens[i][1] == "ILLEGAL":
            #index = sum(len(char) for char, _ in tokens[:i]) - 1 + spaces
            index = characters.index(tokens[i][0])
            print("Lexical error: Statement contains illegal characters at %i: %s (token index: %i)" % (
                index, tokens[i][0], i))
            return False
    return True
