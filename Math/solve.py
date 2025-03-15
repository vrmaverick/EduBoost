from sympy import symbols, Eq, solve

def SolveEquation(eqn):
    eqn = eqn.strip().replace("^", "**")  # Convert '^' to '**' for exponentiation
    # eqn = eqn.strip()  # Remove extra spaces
    
    # Case 1: Arithmetic Expression (e.g., "5+5=")
    if eqn.endswith("="):  
        expression = eqn[:-1].strip()  # Remove '='
        print(f"Result: {eval(expression)}")
        return "none",eval(expression)
    
    # Case 2: Algebraic Equation (e.g., "y+1=2")
    elif "=" in eqn:
        left, right = eqn.split("=")
        left, right = left.strip(), right.strip()

        # Detect variable in the equation
        var_name = ''.join(filter(str.isalpha, left)) or "x"  # Assume 'x' if no variable found
        # print(var_name[0])
        var_name = var_name[0]
        variable = symbols(var_name)
        # print(variable)

        # Solve the equation
        equation = Eq(eval(left, {var_name: variable}), eval(right))
        solution = solve(equation, variable)

        print(f"Solution: {var_name[0]} = {solution[0]}")  # Print first solution
        return var_name[0],solution[0]
    
    # Case 3: Direct Arithmetic Evaluation (e.g., "5+5")
    else:
        print(f"Result: {eval(eqn)}")
        return "none",eval(eqn)

if __name__ == "__main__":
    # a,b = SolveEquation("5+5=")     # Output: Result: 10
    # a,b =SolveEquation("y^2-5*y+6=0")    # Output: Solution: y = 1
    a,b = SolveEquation("3*7")      # Output: Result: 21
    print(a,b)
