def get_used_vars(ir):
    used_vars = set()
    for instr in ir:
        if instr[0] in ("=", "+", "-", "*", ">", "<", "ifnot", "print"):
            for i in range(2, len(instr)):
                if isinstance(instr[i], str) and not instr[i].startswith("L"):
                    used_vars.add(instr[i])
    return used_vars

def constant_folding(ir):
    new_ir = []
    for instr in ir:
        if instr[0] in ("+", "-", "*", ">", "<"):
            op, result, left, right = instr
            try:
                left_val = int(left)
                right_val = int(right)
                if op == "+":
                    new_ir.append(("=", result, str(left_val + right_val)))
                elif op == "-":
                    new_ir.append(("=", result, str(left_val - right_val)))
                elif op == "*":
                    new_ir.append(("=", result, str(left_val * right_val)))
                elif op == ">":
                    new_ir.append(("=", result, str(int(left_val > right_val))))
                elif op == "<":
                    new_ir.append(("=", result, str(int(left_val < right_val))))
            except ValueError:
                new_ir.append(instr)
        else:
            new_ir.append(instr)
    return new_ir

def dead_code_elimination(ir):
    used_vars = get_used_vars(ir)
    optimized_ir = []
    for instr in ir:
        if instr[0] == "=" and instr[1] not in used_vars:
            continue
        optimized_ir.append(instr)
    return optimized_ir

def strength_reduction(ir):
    new_ir = []
    for instr in ir:
        if instr[0] == "*" and isinstance(instr[3], str):
            try:
                val = int(instr[3])
                if val == 2:
                    new_ir.append(("<<", instr[1], instr[2], "1"))
                elif val == 4:
                    new_ir.append(("<<", instr[1], instr[2], "2"))
                else:
                    new_ir.append(instr)
            except ValueError:
                new_ir.append(instr)
        else:
            new_ir.append(instr)
    return new_ir

def loop_invariant_code_motion(ir):
    new_ir = []
    loop_start = None
    loop_end = None
    invariants = []
    in_loop = False

    for i, instr in enumerate(ir):
        if instr[0] == "label" and not in_loop:
            loop_start = instr[1]
            in_loop = True
        elif instr[0] == "label" and in_loop and i > 0 and ir[i-1][0] == "goto" and ir[i-1][1] == loop_start:
            loop_end = instr[1]
            in_loop = False
        elif in_loop and instr[0] in ("+", "-", "*"):
            # Check if operands are loop-invariant (not modified in loop)
            op, result, left, right = instr
            modified_vars = set()
            for j in range(i, len(ir)):
                if ir[j][0] == "=" and ir[j][1] in (left, right):
                    modified_vars.add(ir[j][1])
                if ir[j][0] == "label" and ir[j][1] == loop_end:
                    break
            if left not in modified_vars and right not in modified_vars:
                invariants.append(instr)
                continue
        new_ir.append(instr)

    # Move invariants before loop
    if invariants and loop_start:
        for i, instr in enumerate(new_ir):
            if instr[0] == "label" and instr[1] == loop_start:
                new_ir[i:i] = invariants
                break

    return new_ir

def common_subexpression_elimination(ir):
    new_ir = []
    seen_expressions = {}
    for instr in ir:
        if instr[0] in ("+", "-", "*"):
            op, result, left, right = instr
            expr_key = (op, left, right)
            if expr_key in seen_expressions:
                # Replace with the previous result
                new_ir.append(("=", result, seen_expressions[expr_key]))
            else:
                seen_expressions[expr_key] = result
                new_ir.append(instr)
        else:
            new_ir.append(instr)
    return new_ir

def optimize_ir(ir):
    ir = constant_folding(ir)
    ir = common_subexpression_elimination(ir)
    ir = loop_invariant_code_motion(ir)
    ir = strength_reduction(ir)
    ir = dead_code_elimination(ir)
    return ir