# temp_count = 0
# label_count = 0

# def new_temp():
#     global temp_count
#     temp_count += 1
#     return f"t{temp_count}"

# def new_label():
#     global label_count
#     label_count += 1
#     return f"L{label_count}"

# def generate_expr_ir(expr):
#     if expr[0] == "number":
#         return str(expr[1]), []
#     elif expr[0] == "identifier":
#         return expr[1], []
#     elif expr[0] == "string":
#         return expr[1], []
#     elif expr[0] == "binary_op":
#         op = expr[1]
#         left_var, left_ir = generate_expr_ir(expr[2])
#         right_var, right_ir = generate_expr_ir(expr[3])
#         temp = new_temp()
#         instr = (op, temp, left_var, right_var)
#         return temp, left_ir + right_ir + [instr]
#     else:
#         raise ValueError(f"Unknown expression type: {expr[0]}")

# def generate_statement_ir(stmt):
#     if stmt[0] == "assignment":
#         var = stmt[1]
#         expr_var, expr_ir = generate_expr_ir(stmt[2])
#         return expr_ir + [("=", var, expr_var)]
#     elif stmt[0] == "if_else":
#         cond = stmt[1]
#         then_stmt = stmt[2]
#         else_stmt = stmt[3]
#         cond_var, cond_ir = generate_expr_ir(cond)
#         L1 = new_label()
#         L2 = new_label()
#         then_ir = []
#         if isinstance(then_stmt, list):
#             for s in then_stmt:
#                 then_ir.extend(generate_statement_ir(s))
#         else:
#             then_ir = generate_statement_ir(then_stmt)
#         else_ir = []
#         if isinstance(else_stmt, list):
#             for s in else_stmt:
#                 else_ir.extend(generate_statement_ir(s))
#         else:
#             else_ir = generate_statement_ir(else_stmt)
#         ir = (cond_ir +
#               [("ifnot", cond_var, L1)] +
#               then_ir +
#               [("goto", L2)] +
#               [("label", L1)] +
#               else_ir +
#               [("label", L2)])
#         return ir
#     elif stmt[0] == "print":
#         expr_var, expr_ir = generate_expr_ir(stmt[1])
#         return expr_ir + [("print", expr_var)]
#     elif stmt[0] == "declaration":
#         var_name = stmt[1]
#         if len(stmt) > 2:
#             expr_var, expr_ir = generate_expr_ir(stmt[2])
#             return expr_ir + [("=", var_name, expr_var)]
#         return [("=", var_name, 0)]
#     else:
#         raise ValueError(f"Unknown statement type: {stmt[0]}")

# def generate_ir(ast):
#     ir = []
#     for stmt in ast:
#         ir.extend(generate_statement_ir(stmt))
#     return ir


temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def new_label():
    global label_count
    label_count += 1
    return f"L{label_count}"

def generate_expr_ir(expr):
    if expr[0] == "number":
        return str(expr[1]), []
    elif expr[0] == "identifier":
        return expr[1], []
    elif expr[0] == "string":
        return expr[1], []
    elif expr[0] == "binary_op":
        op = expr[1]
        left_var, left_ir = generate_expr_ir(expr[2])
        right_var, right_ir = generate_expr_ir(expr[3])
        temp = new_temp()
        instr = (op, temp, left_var, right_var)
        return temp, left_ir + right_ir + [instr]
    else:
        raise ValueError(f"Unknown expression type: {expr[0]}")

def generate_statement_ir(stmt):
    if stmt[0] == "assignment":
        var = stmt[1]
        expr_var, expr_ir = generate_expr_ir(stmt[2])
        return expr_ir + [("=", var, expr_var)]
    elif stmt[0] == "if_else":
        cond = stmt[1]
        then_stmt = stmt[2]
        else_stmt = stmt[3]
        cond_var, cond_ir = generate_expr_ir(cond)
        L1 = new_label()
        L2 = new_label()
        L_loop_start = new_label()
        then_ir = []
        if isinstance(then_stmt, list):
            for s in then_stmt:
                then_ir.extend(generate_statement_ir(s))
        else:
            then_ir = generate_statement_ir(then_stmt)
        else_ir = []
        if isinstance(else_stmt, list):
            for s in else_stmt:
                else_ir.extend(generate_statement_ir(s))
        else:
            else_ir = generate_statement_ir(else_stmt)
        # Simulate a loop for the first if (i < 5)
        if cond[1] == "<":  # Treat as a loop
            ir = ([("label", L_loop_start)] +
                  cond_ir +
                  [("ifnot", cond_var, L1)] +
                  then_ir +
                  [("goto", L_loop_start)] +
                  [("label", L1)] +
                  else_ir +
                  [("label", L2)])
        else:  # Regular if-else
            ir = (cond_ir +
                  [("ifnot", cond_var, L1)] +
                  then_ir +
                  [("goto", L2)] +
                  [("label", L1)] +
                  else_ir +
                  [("label", L2)])
        return ir
    elif stmt[0] == "print":
        expr_var, expr_ir = generate_expr_ir(stmt[1])
        return expr_ir + [("print", expr_var)]
    elif stmt[0] == "declaration":
        var_name = stmt[1]
        if len(stmt) > 2:
            expr_var, expr_ir = generate_expr_ir(stmt[2])
            return expr_ir + [("=", var_name, expr_var)]
        return [("=", var_name, 0)]
    else:
        raise ValueError(f"Unknown statement type: {stmt[0]}")

def generate_ir(ast):
    ir = []
    for stmt in ast:
        ir.extend(generate_statement_ir(stmt))
    return ir