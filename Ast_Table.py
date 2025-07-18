import os
import subprocess
from IR import generate_ir

def generate_ast_dot(ast, filename="ast.dot"):
    """Generates a DOT representation of an Abstract Syntax Tree (AST)."""
    if not ast or not isinstance(ast, (list, tuple)):
        print("Invalid AST structure. Cannot generate DOT file.")
        return

    dot_lines = [
        "digraph AST {",
        '    graph [bgcolor=gray];',
        '    node [shape=rectangle, style=filled, fillcolor=lightblue, fontcolor=black, fontsize=14, fontname="Arial"];',
        '    edge [color=black];',
        "\n"
    ]

    def add_node(node, parent_id=None):
        """Recursively adds nodes to the DOT structure."""
        if node is None:
            return
        
        node_id = id(node)
        
        if isinstance(node, list):
            for child in node:
                add_node(child, parent_id)
        
        elif isinstance(node, tuple) and node:
            label = str(node[0]).replace('"', '\\"')
            dot_lines.append(f'    {node_id} [label="{label}"];')
            if parent_id:
                dot_lines.append(f'    {parent_id} -> {node_id};')
            for child in node[1:]:
                add_node(child, node_id)
        
        elif isinstance(node, (int, float, str)):
            label = str(node).replace('"', '\\"')
            dot_lines.append(f'    {node_id} [label="{label}", shape=ellipse, fillcolor=lightyellow];')
            if parent_id:
                dot_lines.append(f'    {parent_id} -> {node_id};')
        
        else:
            dot_lines.append(f'    {node_id} [label="Invalid Node", shape=ellipse, fillcolor=red];')
            if parent_id:
                dot_lines.append(f'    {parent_id} -> {node_id};')
            print(f"Warning: Unexpected AST structure at node {node}")

    add_node(ast)
    dot_lines.append("}")

    # Write DOT file
    with open(filename, "w") as f:
        f.write("\n".join(dot_lines))

    # Convert DOT file to PNG using Graphviz
    output_png = filename.replace(".dot", ".png")
    try:
        subprocess.run(["dot", "-Tpng", filename, "-o", output_png], check=True)
        print(f"Check the PNG: {output_png}")
    except FileNotFoundError:
        print("Graphviz is not installed or 'dot' command not found. Install Graphviz to generate PNG.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to generate PNG from {filename}. Check Graphviz installation and DOT file.")

if __name__ == "__main__":
    try:
        from syntax import parser

        sample_code = '''
            int x = 23;
            int y = 54;
            int z;
            int w = 3 + 5;  
            int unused;     
            z = x * 4;      
            int i = 0;
            int sum = 0;
            int loop_inv = x + y;  
            int temp = x + y;     
            if (i < 5) {           
                sum = sum + loop_inv;
                i = i + 1;
            }
            if (z > 40) {
                print("Result is greater than 40");
                print(temp);
            }
        '''

        # Generate AST
        ast = parser.parse(sample_code)
        print("\nGenerated AST:", ast)

        # Generate DOT file and PNG
        generate_ast_dot(ast, "ast.dot")
        print("AST DOT file and PNG image successfully generated!")

        # Generate IR
        try:
            ir = generate_ir(ast)
            print("\nGenerated IR:")
            for instr in ir:
                print(instr)

            # Save IR to file
            with open("ir.txt", "w") as f:
                for instr in ir:
                    f.write(str(instr) + "\n")
            print("IR saved to ir.txt")
        except ValueError as e:
            print(f"Error generating IR: {e}")
        except Exception as e:
            print(f"Unexpected error during IR generation: {e}")

    except ImportError:
        print("Error: Could not import parser from syntax module.")
    except Exception as e:
        print(f"Error during AST generation: {e}")
