# A simple calculator program

def calculate():
    ans = float(input("enter first num: ")) # <-- the first num is initially equal to the ans 
    
    while True:
        op = input("enter operator: ")
        if op == "=": #<-- breaking the loop if the user asks for the result "="
            break
        sn = float(input("enter next num: ")) #<-- if not ask for the next num

        if op == "-":
            ans -= sn
        elif op == "x":
            ans *= sn
        elif op == "/":
            ans /= sn
        elif op == "+":
            ans += sn
        else:
            print("invalid operator")
    
    print("result = ", ans) 

calculate()
