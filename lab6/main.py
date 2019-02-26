from lex import Lexer
from pparser import Parser, Memory


def printTokenes(tokens):
    for i, tok in enumerate(tokens):
        print(i, '=', tok)


def printMemory(memory):
    print(memory)


if __name__ == "__main__":

    fname = "test"
    with open(fname) as f:
        text_input = f.read()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens)
    printMemory(Memory)
