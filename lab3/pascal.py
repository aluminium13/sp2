import lex

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"  # add, foobar, x, y
INT = "INT"
STRING = "STRING"

# Operators
ASSIGN = "OPERATOR: :="
PLUS = "OPERATOR: +"
MINUS = "OPERATOR: -"
BANG = "OPERATOR: !"
ASTERISK = "OPERATOR: *"
SLASH = "OPERATOR: /"
LT = "OPERATOR: <"
GT = "OPERATOR: >"
EQ = "OPERATOR: =="
NOTEQ = "OPERATOR: !="
DQUOTE = "OPERATOR: \""
SQUOTE = "OPERATOR: '"

# Delimiters
COMMA = "DELIMITER: ,"
SEMICOLON = "DELIMITER: ;"

LPAREN = "LEFT PAREN: ("
RPAREN = "RIGHT PAREN: )"
LBRACE = "LEFT BRACE: ["
RBRACE = "RIGHT BRACE: ]"

# keywords
NOT = "KEYWORD: NOT"
NIL = "KEYWORD: NIL"
TRUE = "KEYWORD: TRUE"
FALSE = "KEYWORD: FALSE"
FOR = "KEYWORD: FOR"
WHILE = "KEYWORD: WHILE"
DO = "KEYWORD: DO"
IF = "KEYWORD: IF"
ELSE = "KEYWORD: ELSE"
THEN = "KEYWORD: THEN"
END = "KEYWORD: END"
AND = "KEYWORD: AND"
REPEAT = "KEYWORD: REPEAT"
BEGIN = "KEYWORD: BEGIN"
UNTIL = "KEYWORD: UNTIL"

token_expressions = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'not',                   NOT),
    (r'nil',                   NIL),
    (r':=',                    ASSIGN),
    (r'=',                     EQ),
    (r'!=',                    "Illigal character"),
    (r'and',                   AND),
    (r'while ',                WHILE),
    (r'do ',                   DO),
    (r'for ',                  FOR),
    (r'if ',                   IF),
    (r'then ',                 THEN),
    (r'else',                  ELSE),
    (r'end ',                  END),
    (r'repeat ',                REPEAT),
    (r'begin ',                 BEGIN),
    (r'until ',                 UNTIL),
    (r'\(',                    LPAREN),
    (r'\)',                    RPAREN),
    (r'\+',                    PLUS),
    (r'\*',                     ASTERISK),
    (r'-',                     MINUS),
    (r';',                     SEMICOLON),
    (r'<',                     LT),
    (r'>',                     GT),
    (r'\[',                    LBRACE),
    (r'\]',                    RBRACE),
    (r'array',                "KEYWORD: ARRAY"),
    (r'break',                "KEYWORD: BREAK"),
    (r'continue',             "KEYWORD: CONTINUE"),
    (r'exit',                 "KEYWORD: EXIT"),
    (r'function',             "KEYWORD: FUNCTION"),
    (r'boolean',              "KEYWORD: BOOLEAN"),
    (r'var',                  "KEYWORD: VAR"),
    (r'\&',                     'OERATOR: AND'),
    (r'[0-9_]+[A-Za-z_]+',      ILLEGAL),
    (r'[0-9]+\.[0-9]+',         'DATA_TYPE: FLOAT'),
    (r'[0-9]+\.[^0-9]+',        ILLEGAL),
    (r'[A-Za-z]+\.[A-Za-z|0-9]+', ILLEGAL),
    (r'[0-9]+',                 INT),
    (r'[^A-Za-z][A-Za-z0-9_]*', ILLEGAL),
    (r'[A-Za-z][A-Za-z0-9_]*',  IDENT),

]


def pascal_lex(data):
    return lex.lex(data, token_expressions)
