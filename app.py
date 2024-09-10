from flask import Flask, render_template, request
import math
import sympy as sp

app = Flask(__name__)

# Function to handle algebraic expression evaluation
def calculate_expression(expression):
    try:
        # Handling algebraic expressions using SymPy
        if any(char.isalpha() for char in expression):
            x, y, z = sp.symbols('x y z')  # Define symbols for algebraic variables
            algebraic_result = sp.simplify(expression)  # Simplify the algebraic expression
            return str(algebraic_result)
        # Handling normal math operations (without variables)
        elif '!' in expression:  # Handling factorial
            num = int(expression.replace('!', ''))
            result = math.factorial(num)
        else:
            result = eval(expression, {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
                                       "tan": math.tan, "log": math.log, "exp": math.exp,
                                       "pi": math.pi, "e": math.e, "__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expression = request.form["expression"]
        result = calculate_expression(expression)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
