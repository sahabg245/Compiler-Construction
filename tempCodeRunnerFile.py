
import os
import subprocess
from lexer import lexer
from syntax import parser
from semantic import analyze
from Ast_Table import generate_ast_dot
from IR import generate_ir
from OC import optimize_ir

if __name__ == "__main__":
    base_dir = r"C:\Users\abdul\OneDrive\Desktop\CC"
    input_file = os.path.join(base_dir, "test_code.txt")
    ir_file = os.path.join(base_dir, "ir.txt")
    optimized_ir_file = os.path.join(base_dir, "optimized_ir.txt")
    ast_dot_file = os.path.join(base_dir, "ast.dot")

    try:
        print(f"Reading input from {input_file}")
        with open(input_file, "r") as file:
            data = file.read()
        
        print("\n      Lexical Analysis ")
        lexer.input(data)
        for tok in lexer:
            print(tok)

        print("\n      Syntax Analysis ")
        ast = parser.parse(data, lexer=lexer)
        if ast is None:
            print("Error: Parsing failed, AST is None.")
            exit(1)
        print("Generated AST:", ast)

        print("\n      Semantic Analysis ")
        semantic_passed = False
        try:
            analyze(ast)
            semantic_passed = True
        except Exception as e:
            print(f"Semantic Error: {e}. Continuing to later phases for debugging.")

        print("\n       AST Visualization        ")
        try:
            # Check if ast.dot already exists
            if os.path.exists(ast_dot_file):
                print(f"Warning: {ast_dot_file} already exists, overwriting.")
            # Check if we can write to the directory
            test_file = os.path.join(base_dir, "test_write.txt")
            with open(test_file, "w") as f:
                f.write("test")
            print(f"Successfully wrote test file to {test_file}")
            os.remove(test_file)
            # Generate AST visualization
            if not generate_ast_dot(ast, filename=ast_dot_file):
                print("Failed to generate AST visualization, but continuing.")
            else:
                print("AST visualization generated successfully.")
                print(f"Check the PNG: {ast_dot_file.replace('.dot', '.png')}")
                # Verify PNG exists
                png_file = ast_dot_file.replace('.dot', '.png')
                if os.path.exists(png_file):
                    print(f"Confirmed: {png_file} exists.")
                else:
                    print(f"Error: {png_file} was not created.")
        except Exception as e:
            print(f"AST Visualization Error: {e}. Continuing to IR generation.")

        print("\n       Intermediate Representation (IR) Generation ")
        try:
            ir = generate_ir(ast)
            print("IR Instructions:")
            with open(ir_file, "w") as f:
                for instr in ir:
                    print(instr)
                    f.write(str(instr) + "\n")
            print(f"IR saved to {ir_file}")
        except Exception as e:
            print(f"IR Generation Error: {e}. Continuing to optimization.")

        print("\n      Optimized IR ")
        try:
            optimized_ir = optimize_ir(ir)
            print("Optimized IR Instructions:")
            with open(optimized_ir_file, "w") as f:
                for instr in optimized_ir:
                    print(instr)
                    f.write(str(instr) + "\n")
            print(f"Optimized IR saved to {optimized_ir_file}")
        except Exception as e:
            print(f"IR Optimization Error: {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except ImportError as e:
        print(f"Import Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        exit(1)