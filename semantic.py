# # semantic.py
# def analyze(ast):
#     symbol_table = {}

#     def check_expr(expr):
#         if expr[0] == 'number':
#             return 'int'
#         elif expr[0] == 'identifier':
#             if expr[1] not in symbol_table:
#                 raise ValueError(f"Undefined variable '{expr[1]}'")
#             return symbol_table[expr[1]]
#         elif expr[0] == 'string':
#             return 'string'
#         elif expr[0] == 'binary_op':
#             left_type = check_expr(expr[2])
#             right_type = check_expr(expr[3])
#             op = expr[1]
#             if op in ('+', '>', '=='):
#                 if left_type != 'int' or right_type != 'int':
#                     raise ValueError(f"Type mismatch in '{op}' operation: {left_type} and {right_type}")
#                 return 'int' if op == '+' else 'bool'
#             else:
#                 raise ValueError(f"Unsupported operator '{op}'")
#         else:
#             raise ValueError(f"Unknown expression type: {expr[0]}")

#     def check_stmt(stmt):
#         if stmt[0] == 'declaration':
#             var = stmt[1]
#             if var in symbol_table:
#                 raise ValueError(f"Redefinition of variable '{var}'")
#             if len(stmt) > 2:
#                 expr_type = check_expr(stmt[2])
#                 symbol_table[var] = expr_type
#             else:
#                 symbol_table[var] = 'int'
#         elif stmt[0] == 'assignment':
#             var = stmt[1]
#             if var not in symbol_table:
#                 raise ValueError(f"Undefined variable '{var}' in assignment")
#             expr_type = check_expr(stmt[2])
#             if symbol_table[var] != expr_type:
#                 raise ValueError(f"Type mismatch in assignment to '{var}': expected {symbol_table[var]}, got {expr_type}")
#         elif stmt[0] == 'if_else':
#             cond_type = check_expr(stmt[1])
#             if cond_type != 'bool':
#                 raise ValueError(f"If condition must be boolean, got {cond_type}")
#             for s in stmt[2]:
#                 check_stmt(s)
#             for s in stmt[3]:
#                 check_stmt(s)
#         elif stmt[0] == 'print':
#             check_expr(stmt[1])
#         else:
#             raise ValueError(f"Unknown statement type: {stmt[0]}")

#     if ast is None:
#         raise ValueError("Invalid AST: None")
#     for stmt in ast:
#         check_stmt(stmt)
#     print("Semantic analysis passed")


# def analyze(ast):
#     """Perform semantic analysis on the AST with detailed logging."""
#     symbol_table = {}
#     print("Semantic Analysis:")

#     def check_expr(expr):
#         if expr[0] == 'number':
#             print(f"- Expression 'number {expr[1]}': type 'int'")
#             return 'int'
#         elif expr[0] == 'identifier':
#             if expr[1] not in symbol_table:
#                 raise ValueError(f"Undefined variable '{expr[1]}'")
#             print(f"- Expression 'identifier {expr[1]}': type '{symbol_table[expr[1]]}'")
#             return symbol_table[expr[1]]
#         elif expr[0] == 'string':
#             print(f"- Expression 'string \"{expr[1]}\"': type 'string'")
#             return 'string'
#         elif expr[0] == 'binary_op':
#             left_type = check_expr(expr[2])
#             right_type = check_expr(expr[3])
#             op = expr[1]
#             if op in ('+', '>', '=='):
#                 if left_type != 'int' or right_type != 'int':
#                     raise ValueError(f"Type mismatch in '{op}' operation: {left_type} ({expr[2]}) and {right_type} ({expr[3]})")
#                 result_type = 'int' if op == '+' else 'bool'
#                 print(f"- Binary operation '{op}' with operands '{left_type}' and '{right_type}': result type '{result_type}'")
#                 return result_type
#             else:
#                 raise ValueError(f"Unsupported operator '{op}'")
#         else:
#             raise ValueError(f"Unknown expression type: {expr[0]}")

#     def check_stmt(stmt):
#         if stmt[0] == 'declaration':
#             var = stmt[1]
#             if var in symbol_table:
#                 raise ValueError(f"Redefinition of variable '{var}'")
#             if len(stmt) > 2:
#                 expr_type = check_expr(stmt[2])
#                 symbol_table[var] = expr_type
#                 print(f"- Variable '{var}' declared as type '{expr_type}'")
#             else:
#                 symbol_table[var] = 'int'
#                 print(f"- Variable '{var}' declared as type 'int'")
#         elif stmt[0] == 'assignment':
#             var = stmt[1]
#             if var not in symbol_table:
#                 raise ValueError(f"Undefined variable '{var}' in assignment")
#             expr_type = check_expr(stmt[2])
#             if symbol_table[var] != expr_type:
#                 raise ValueError(f"Type mismatch in assignment to '{var}': expected {symbol_table[var]}, got {expr_type}")
#             print(f"- Assignment to '{var}': expected type '{symbol_table[var]}', got type '{expr_type}'")
#         elif stmt[0] == 'if_else':
#             cond_type = check_expr(stmt[1])
#             if cond_type != 'bool':
#                 raise ValueError(f"If condition must be boolean, got {cond_type}")
#             print(f"- If condition: type '{cond_type}'")
#             for s in stmt[2]:
#                 check_stmt(s)
#             for s in stmt[3]:
#                 check_stmt(s)
#         elif stmt[0] == 'print':
#             expr_type = check_expr(stmt[1])
#             print(f"- Print statement: expression type '{expr_type}'")
#         else:
#             raise ValueError(f"Unknown statement type: {stmt[0]}")

#     if ast is None:
#         raise ValueError("Invalid AST: None")
#     for stmt in ast:
#         check_stmt(stmt)
#     print("Semantic analysis passed")


#############################

def analyze(ast):
    """Perform semantic analysis on the AST with detailed logging."""
    symbol_table = {}
    print("Semantic Analysis:")

    def check_expr(expr):
        if expr[0] == 'number':
            print(f"- Expression 'number {expr[1]}': type 'int'")
            return 'int'
        elif expr[0] == 'identifier':
            if expr[1] not in symbol_table:
                raise ValueError(f"Undefined variable '{expr[1]}'. Symbol table: {symbol_table}")
            print(f"- Expression 'identifier {expr[1]}': type '{symbol_table[expr[1]]}'")
            return symbol_table[expr[1]]
        elif expr[0] == 'string':
            print(f"- Expression 'string \"{expr[1]}\"': type 'string'")
            return 'string'
        elif expr[0] == 'binary_op':
            left_type = check_expr(expr[2])
            right_type = check_expr(expr[3])
            op = expr[1]
            if op in ('+', '*', '>', '<', '=='):
                if left_type != 'int' or right_type != 'int':
                    raise ValueError(f"Type mismatch in '{op}' operation: {left_type} ({expr[2]}) and {right_type} ({expr[3]})")
                result_type = 'int' if op in ('+', '*') else 'bool'
                print(f"- Binary operation '{op}' with operands '{left_type}' and '{right_type}': result type '{result_type}'")
                return result_type
            else:
                raise ValueError(f"Unsupported operator '{op}'")
        else:
            raise ValueError(f"Unknown expression type: {expr[0]}")

    def check_stmt(stmt):
        if stmt[0] == 'declaration':
            var = stmt[1]
            if var in symbol_table:
                raise ValueError(f"Redefinition of variable '{var}'")
            if len(stmt) > 2:
                expr_type = check_expr(stmt[2])
                symbol_table[var] = expr_type
            else:
                symbol_table[var] = 'int'
            print(f"- Variable '{var}' declared as type '{symbol_table[var]}'")
            print(f"  Symbol table after declaration: {symbol_table}")
        elif stmt[0] == 'assignment':
            var = stmt[1]
            if var not in symbol_table:
                raise ValueError(f"Undefined variable '{var}' in assignment. Symbol table: {symbol_table}")
            expr_type = check_expr(stmt[2])
            if symbol_table[var] != expr_type:
                raise ValueError(f"Type mismatch in assignment to '{var}': expected {symbol_table[var]}, got {expr_type}")
            print(f"- Assignment to '{var}': expected type '{symbol_table[var]}', got type '{expr_type}'")
        elif stmt[0] == 'if_else':
            cond_type = check_expr(stmt[1])
            if cond_type != 'bool':
                raise ValueError(f"If condition must be boolean, got {cond_type}")
            print(f"- If condition: type '{cond_type}'")
            for s in stmt[2]:
                check_stmt(s)
            for s in stmt[3]:
                check_stmt(s)
        elif stmt[0] == 'print':
            expr_type = check_expr(stmt[1])
            print(f"- Print statement: expression type '{expr_type}'")
        else:
            raise ValueError(f"Unknown statement type: {stmt[0]}")

    if ast is None:
        raise ValueError("Invalid AST: None")
    for stmt in ast:
        check_stmt(stmt)
    print("Semantic analysis passed")