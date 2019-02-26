import sys
import re


def lex(characters, token_exprs):
    pos = 0
    tokens = []
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
            token = (characters[pos], "Illegal character")
            tokens.append(token)
            return tokens
        else:
            pos = match.end(0)


    return tokens

def hasNoErrors(tokens):
        for _, j in tokens:
            if j == "ILLEGAL":
                print("Statement contains illegal characters")
                return False
        return True