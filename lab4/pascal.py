import lex

ILLEGAL = "ILLEGAL"
EOF     = "EOF"

# Identifiers + literals
IDENT  = "IDENT"  
INT    = "INT"
FLOAT  = "FLOAT"
STRING = "STRING"

# Operators 
ASSIGN   = "Operator: :="
PLUS     = "Operator: +"
MINUS    = "Operator: -"
ASTERISK = "Operator: *"
SLASH    = "Operator: /"
LT       = "Operator: <"
GT       = "Operator: >"
EQ       = "Operator: ="
NOTEQ    = "Operator: <>"

DQUOTE   = "\""
SQUOTE   = "'"

# Delimiters
COMMA     = "Delimiter ,"
SEMICOLON = "Delimiter ;"

# Brackets
LPAREN = "Bracket: ("
RPAREN = "Bracket: )"
LBRACE = "Bracket: ["
RBRACE = "Bracket: ]"

# Keywords
AND   = "Keyword: AND"
TRUE  = "Keyword: TRUE"
FALSE = "Keyword: FALSE"
FOR   = "Keyword: FOR"
WHILE = "Keyword: WHILE"
DO    = "Keyword: DO"
IF    = "Keyword: IF"
ELSE  = "Keyword: ELSE"
THEN  = "Keyword: THEN"
END   = "Keyword: END"
BEGIN = 'Keyword: BEGIN'
BREAK = 'Keyword: BREAK'
CASE  = 'Keyword: CASE'
DIV   = 'Keyword: DIV'
DOWNTO= 'Keyword: DOWNTO'

token_expressions = [
    (r'[ \n\t]+',                None),
    (r'#[^\n]*',                 None),
    (r':=',                      ASSIGN),
    (r'=',                       EQ),
    (r'<>',                      NOTEQ),
    (r'and',                     AND),
    (r'while ',                  WHILE),
    (r'for ',                    FOR),
    (r'if ',                     IF),
    (r'then ',                   THEN),
    (r'else',                   ELSE),
    (r'begin',                   BEGIN),
    (r'end ',                    END),
    (r'break',                   BREAK),
    (r'case',                    CASE),
    (r'div',                     DIV),
    (r'downto',                  DOWNTO),
    (r'do ',                     DO),
    (r'function',               'Keyword: FUNCTION'),
    (r'goto',                   'Keyword: GOTO'),
    (r'nil',                    'DATA_TYPE: INT'),
    (r'or',                     'Operator: OR'),
    (r'not',                    'Keyword: NOT'),
    (r'procedure',              'Keyword: PROCEDURE'),
    (r'repeat',                 'Keyword: REPEAT'),
    (r'string',                 'DATA_TYPE: STRING'),
    (r'to',                     'Keyword: TO'),
    (r'until',                  'Keyword: UNTIL'),
    (r'type',                   'Keyword: TYPE'),
    (r'var',                    'Keyword: VAR'),
    (r'xor',                    'Operator: XOR'),
    (r'\!=',                     ILLEGAL),
    (r'\!',                     'Operator: NOT'),
    (r'\(',                      LPAREN),
    (r'\)',                      RPAREN),
    (r'\+',                      PLUS),
    (r'-',                       MINUS),
    (r'\*',                      ASTERISK),
    (r';',                       SEMICOLON),
    (r'<',                       LT),
    (r'>',                       GT),
    (r'\[',                      LBRACE),
    (r'\]',                      RBRACE),
    (r'\&',                      AND),
    (r'[0-9_]+[A-Za-z_]+',       ILLEGAL),
    (r'[0-9]+\.[0-9]+',          FLOAT),
    (r'[0-9]+\.[^0-9]+',         ILLEGAL),
    (r'[A-Za-z]+\.[A-Za-z|0-9]+',ILLEGAL),
    (r'[0-9]+',                  INT),
    (r'[^A-Za-z][A-Za-z0-9_]*',  ILLEGAL),
    (r'[A-Za-z][A-Za-z0-9_]*',   IDENT),
]

def pascal_lex(data):
    return lex.lex(data, token_expressions)
