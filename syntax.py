# import ply.yacc as yacc
# from lexer import tokens

# def p_program(p):
#     '''program : statement_list'''
#     p[0] = p[1]

# def p_statement_list(p):
#     '''statement_list : statement
#                       | statement_list statement
#                       | '''
#     if len(p) == 1:
#         p[0] = []
#     elif len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[2]]

# def p_statement(p):
#     '''statement : declaration
#                  | assignment
#                  | if_statement
#                  | print_statement'''
#     p[0] = p[1]

# def p_declaration(p):
#     '''declaration : INT ID SEMICOLON
#                    | INT ID ASSIGN expression SEMICOLON
#                    | STRING_KW ID ASSIGN STRING SEMICOLON'''
#     if len(p) == 4 and p[1] == 'int':
#         p[0] = ('declaration', p[2])
#     elif len(p) == 6 and p[1] == 'int':
#         p[0] = ('declaration', p[2], ('number', p[4]))
#     elif len(p) == 6 and p[1] == 'string':
#         p[0] = ('declaration', p[2], ('string', p[4][1:-1]))
#     else:
#         print(f"Syntax Error: Invalid declaration at line {p.lineno(1)}")
#         p[0] = None

# def p_assignment(p):
#     '''assignment : ID ASSIGN expression SEMICOLON'''
#     p[0] = ('assignment', p[1], p[3])

# def p_if_statement(p):
#     '''if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE
#                     | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
#     if len(p) == 8:
#         p[0] = ('if_else', p[3], p[6], [])
#     else:
#         p[0] = ('if_else', p[3], p[6], p[10])

# def p_print_statement(p):
#     '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
#     p[0] = ('print', p[3])

# def p_expression(p):
#     '''expression : NUMBER
#                   | ID
#                   | STRING
#                   | expression PLUS expression
#                   | expression EQ expression
#                   | expression GT expression'''
#     if len(p) == 2:
#         if isinstance(p[1], (int, float)):
#             p[0] = ('number', p[1])
#         elif isinstance(p[1], str) and not p[1].startswith('"'):
#             p[0] = ('identifier', p[1])
#         else:
#             p[0] = ('string', p[1][1:-1])
#     else:
#         p[0] = ('binary_op', p[2], p[1], p[3])

# def p_error(p):
#     if p:
#         print(f"Syntax Error at '{p.value}' (Line {p.lineno})")
#     else:
#         print("Syntax Error at EOF")

# parser = yacc.yacc()


#####################

from ply import yacc
from lexer import tokens

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_stmt
                 | print_stmt'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : INT ID SEMICOLON
                   | INT ID ASSIGN expression SEMICOLON
                   | STRING_KW ID ASSIGN STRING SEMICOLON'''
    if len(p) == 4 and p[1] == 'int':
        p[0] = ('declaration', p[2])
    elif len(p) == 6 and p[1] == 'int':
        p[0] = ('declaration', p[2], p[4])
    elif len(p) == 6 and p[1] == 'string':
        p[0] = ('declaration', p[2], ('string', p[4][1:-1]))
    else:
        print(f"Syntax Error: Invalid declaration at line {p.lineno(1)}")
        p[0] = None

def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expression RPAREN LBRACE statement_list RBRACE
               | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 8:
        p[0] = ('if_else', p[3], p[6], [])
    else:
        p[0] = ('if_else', p[3], p[6], p[10])

def p_print_stmt(p):
    '''print_stmt : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('print', p[3])

def p_expression(p):
    '''expression : NUMBER
                  | ID
                  | STRING
                  | binary_op'''
    if isinstance(p[1], (int, float)):
        p[0] = ('number', p[1])
    elif isinstance(p[1], str) and p[1].startswith('"'):
        p[0] = ('string', p[1][1:-1])
    elif isinstance(p[1], str):
        p[0] = ('identifier', p[1])
    else:
        p[0] = p[1]

def p_binary_op(p):
    '''binary_op : expression PLUS expression
                 | expression MINUS expression
                 | expression TIMES expression
                 | expression DIVIDE expression
                 | expression GT expression
                 | expression LT expression
                 | expression EQ expression'''
    p[0] = ('binary_op', p[2], p[1], p[3])

def p_error(p):
    if p:
        print(f"Syntax Error at '{p.value}' (Line {p.lineno})")
    else:
        print("Syntax Error: Unexpected end of input")

parser = yacc.yacc()