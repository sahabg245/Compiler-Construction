# import ply.lex as lex

# reserved = {
#     'int': 'INT',
#     'float': 'FLOAT',
#     'bool': 'BOOL',
#     'string': 'STRING_KW',
#     'if': 'IF',
#     'else': 'ELSE',
#     'while': 'WHILE',
#     'for': 'FOR',
#     'switch': 'SWITCH',
#     'case': 'CASE',
#     'print': 'PRINT',
#     'return': 'RETURN'
# }

# tokens = [
#     'ID', 'NUMBER', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
#     'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'ASSIGN',
#     'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ', 'AND', 'OR', 'NOT'
# ] + list(reserved.values())

# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_SEMICOLON = r';'
# t_ASSIGN = r'='
# t_EQ = r'=='
# t_NEQ = r'!='
# t_LT = r'<'
# t_GT = r'>'
# t_LEQ = r'<='
# t_GEQ = r'>='
# t_AND = r'&&'
# t_OR = r'\|\|'
# t_NOT = r'!'
# t_STRING = r'"[^"]*"'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     t.type = reserved.get(t.value, 'ID')
#     return t

# def t_NUMBER(t):
#     r'\d+\.\d+|\d+'
#     t.value = float(t.value) if '.' in t.value else int(t.value)
#     return t

# t_ignore = ' \t'

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_COMMENT(t):
#     r'(/\*[\s\S]*?\*/|//[^\n]*)'
#     pass

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
#     t.lexer.skip(1)

# lexer = lex.lex()


################
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