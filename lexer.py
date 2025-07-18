
from ply import lex

tokens = (
    'INT', 'STRING_KW', 'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'IF', 'ELSE', 'PRINT', 'GT', 'LT', 'EQ'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='

def t_INT(t):
    r'int'
    return t

def t_STRING_KW(t):
    r'string'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

t_ignore = ' \t\n'

def t_comment(t):
    r'\#.*'
    pass  

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()