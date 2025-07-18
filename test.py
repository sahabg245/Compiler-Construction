from syntax import parser
from Ast_Table import generate_ast_dot
from lexer import lexer

code = """
int x = 5;
if (x > 3) {
    x = x + 1;
}
"""

lexer.input(code)
print("\n--- Lexer Tokens ---")
for tok in lexer:
    print(tok)


ast = parser.parse(code)
print("Generated AST:", ast)

if ast:
    generate_ast_dot(ast)
else:
    print("AST generation failed!")
