import sys
import re


def lex(characters, token_exprs):
    #    p = re.compile(r'[a-zA-Z]+\([^\)]*\)(\.[^\)]*\))?')
    #    characters = p.sub('_call', characters)
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
                    text = text.strip()
                    tag = tag.strip()
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print("Illegal character %s" % characters[pos])
            tokens.append((characters[pos], 'ILLEGAL'))
            # return tokens
        else:
            pos = match.end(0)

    return tokens
