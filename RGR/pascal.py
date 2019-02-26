import lex

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"  # add, foobar, x, y
INT = "int "

# Operators
ASSIGN = ":="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"
LT = "<"
GT = ">"
EQ = "="
NOTEQ = "!="
DQUOTE = "\""
SQUOTE = "'"
DOT = "."

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
LBRACKET = "["
RBRACKET = "]"
VOID = "VOID"

# Keywords
BEGIN = "BEGIN"
TRUE = "TRUE"
FALSE = "FALSE"
FOR = "FOR"
WHILE = "WHILE"
DO = "DO"
IF = "IF"
ELSE = "ELSE"
THEN = "THEN"
END = "END"
AND = "AND"
OR = "OR"
DOUBLE_TYPE = "DOUBLE_TYPE"
INT_TYPE = "INT_TYPE"
BOOL_TYPE = "BOOL_TYPE"
LONG_TYPE = "LONG_TYPE"
FUNCTION = "function"

token_expressions = [
    (r'[ \n\t]+',               None),
    (r'#[^\n]*',                None),
    (r'!=',                     NOTEQ),
    (r':=',                     ASSIGN),
    (r'=',                      EQ),
    (r'and',                    AND),
    (r'or',                     OR),
    (r'while ',                 WHILE),
    (r'do ',                    DO),
    (r'else',                   ELSE),
    (r'for ',                   FOR),
    (r'print',                 'print'),
    (r'if ',                    IF),
    (r'then ',                  THEN),
    (r'end ',                   END),
    (r'void',                   VOID),
    (r'bool ',                  BOOL_TYPE),
    (r'int ',                   INT_TYPE),
    (r'double ',                DOUBLE_TYPE),
    (r'long ',                  LONG_TYPE),
    (r'begin',                  BEGIN),
    (r'end',                    'END'),
    (r'\(',                     LPAREN),
    (r'\)',                     RPAREN),
    (r'\+',                     PLUS),
    (r'\*',                     ASTERISK),
    (r'/',                      SLASH),
    (r'-',                      MINUS),
    (r';',                      SEMICOLON),
    (r',',                      COMMA),
    (r'<',                      LT),
    (r'>',                      GT),
    (r'\{',                     LBRACE),
    (r'\}',                     RBRACE),
    (r'[0-9]*\.[0-9]*',         'double '),
    (r'[0-9]+',                 INT),
    (r'\.',                     DOT),
    (r'_call', FUNCTION),
    (r'[A-Za-z][A-Za-z0-9_]*\[[0-9]+\]', IDENT),
    (r'[A-Za-z][A-Za-z0-9_]*',  IDENT),
]


def pascal_lex(data):
    return lex.lex(data, token_expressions)
