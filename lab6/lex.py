from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT',   r'print')
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('TYPE',    r'type')
        self.lexer.add('VAR',     r'var')
        self.lexer.add('ARRAY',   r'array')
        self.lexer.add('OF',      r'of')
        self.lexer.add('FOR',     r'for')
        self.lexer.add('TO',      r'to')
        self.lexer.add('IF',      r'if')
        self.lexer.add('ELSE',    r'else')
        self.lexer.add('THEN',    r'then')
        self.lexer.add('AND',     r'and')
        self.lexer.add('OR',      r'or')
        self.lexer.add('NOT',     r'not')
        self.lexer.add('BEGIN',   r'begin')
        self.lexer.add('END',     r'end')
        self.lexer.add('ITYPE',   r'integer')
        self.lexer.add('FTYPE',   r'double')
        self.lexer.add('DO',      r'do')
        self.lexer.add('BTYPE',   r'boolean')
        self.lexer.add('FUNCTION',r'function')
        self.lexer.add('BOOLEAN', r'(true|false)')
        # Parenthesis
        self.lexer.add('OPEN_PAREN',  r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Brackets
        self.lexer.add('OPEN_BRACKET',  r'\[')
        self.lexer.add('CLOSE_BRACKET', r'\]')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Assignment
        self.lexer.add('ASSIGNMENT', r'\:\=')
        self.lexer.add('COLON',      r'\:')
        # Delimiters
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('RANGE', r'\.\.')
        self.lexer.add('DOT',   r'\.')
        # Operators
        self.lexer.add('EQUAL',   r'\=')
        self.lexer.add('SUM',     r'\+')
        self.lexer.add('SUB',     r'\-')
        self.lexer.add('MUL',     r'\*')
        self.lexer.add('DIV',     r'\/')
        self.lexer.add('POINTER', r'\^')
        self.lexer.add('NEQUAL',  r'\<\>')
        self.lexer.add('LESS',    r'\<')
        self.lexer.add('MORE',    r'\>')
        # Number
        self.lexer.add('FTYPE', r'[0-9]+\.[0-9]+')
        self.lexer.add('ITYPE', r'\d+')
        # Ignore spaces
        self.lexer.add('ID',  r'\w+')
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
