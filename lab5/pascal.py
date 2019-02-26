import lex

# System types
ILLEGAL = "ILLEGAL"
EOF     = "EOF"

# Identifiers + literals
IDENT  = "IDENT"  

INT    = "Data_type: INT"
FLOAT  = "Data_type: FLOAT"
STRING = "Data_type: STRING"
Data_types = [INT, FLOAT, STRING]

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
NOT      = 'Operator: NOT'
AND      = "Operator: AND"
OR       = 'Operator: OR'
XOR      = 'Operator: XOR'
Operators = [PLUS, MINUS, ASTERISK, SLASH, LT, GT, EQ, NOTEQ, NOT, OR, XOR, AND]

# Quotes
DQUOTE   = "\""
SQUOTE   = "'"
Quotes = [DQUOTE, SQUOTE]

# Delimiters
COMMA     = "Delimiter ,"
SEMICOLON = "Delimiter ;"

# Brackets
LPAREN = "Bracket: ("
RPAREN = "Bracket: )"
LBRACE = "Bracket: ["
RBRACE = "Bracket: ]"

# Keywords

TRUE  = "Keyword: TRUE"
FALSE = "Keyword: FALSE"

BooleanKeywords = [TRUE, FALSE]

FOR     = "Keyword: FOR"
WHILE   = "Keyword: WHILE"
DO      = "Keyword: DO"
IF      = "Keyword: IF"
ELSE    = "Keyword: ELSE"
THEN    = "Keyword: THEN"
BEGIN   = 'Keyword: BEGIN'
END     = "Keyword: END"
BREAK   = 'Keyword: BREAK'
CASE    = 'Keyword: CASE'
DIV     = 'Keyword: DIV'
DOWNTO  = 'Keyword: DOWNTO'
GOTO    = 'Keyword: GOTO'
REPEAT  = 'Keyword: REPEAT'
TO      = 'Keyword: TO'
UNTIL   = 'Keyword: UNTIL'
VAR     = 'Keyword: VAR'
TYPE    = 'Keyword: TYPE'
FUNCTION = 'Keyword: FUNCTION'
PROCEDURE = 'Keyword: PROCEDURE'

Keywords = [FOR, WHILE, DO, IF, ELSE, THEN, BEGIN, END, BREAK, CASE, DIV, DOWNTO, FUNCTION, GOTO, PROCEDURE, REPEAT, TO, UNTIL, VAR, TYPE]

token_expressions = [
    (r'[ \n\t]+',                None),
    (r'#[^\n]*',                 None),
    (r'\+',                      PLUS),
    (r'-',                       MINUS),
    (r'\*',                      ASTERISK),
    (r'//',                      SLASH),
    (r':=',                      ASSIGN),
    (r'=',                       EQ),
    (r'<>',                      NOTEQ),
    (r'<',                       LT),
    (r'>',                       GT),
    (r'and ',                    AND),
    (r'\& ',                     AND),
    (r'not ',                    NOT),
    (r'\!=',                     ILLEGAL),
    (r'\!',                      NOT),
    (r'or ',                     OR),
    (r'xor ',                    XOR),
    (r'nil ',                    INT),
    (r'true ',                   TRUE),
    (r'false ',                  FALSE),
    (r'while',                   WHILE),
    (r'for',                     FOR),
    (r'if',                      IF),
    (r'then',                    THEN),
    (r'else',                    ELSE),
    (r'begin',                   BEGIN),
    (r'end',                     END),
    (r'break',                   BREAK),
    (r'case',                    CASE),
    (r'div',                     DIV),
    (r'downto',                  DOWNTO),
    (r'do',                      DO),
    (r'function',                FUNCTION),
    (r'goto',                    GOTO),
    (r'procedure',               PROCEDURE),
    (r'repeat',                  REPEAT),
    (r'string',                  STRING),
    (r'to',                      TO),
    (r'until',                   UNTIL),
    (r'type',                    TYPE),
    (r'var',                     VAR),
    (r'\(',                      LPAREN),
    (r'\)',                      RPAREN),
    (r';',                       SEMICOLON),
    (r'\[',                      LBRACE),
    (r'\]',                      RBRACE),
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
