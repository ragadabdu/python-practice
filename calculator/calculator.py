# A simple calculator program

def calculate():
    expr = input("Enter an expression (e.g. 2 + 3 * 4 - 5): ")
    try:
        result = eval(expr) #<--evaluates string as python code
        print("Result =", result)
    except Exception as e:
        print("Error:", e)

