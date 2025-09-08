# A simple calculator program

fn = float(input("enter first num: "))
ans = fn

while True:
    op = input("enter operator: ")
    if op == "=":
        break
    sn = float(input("enter next num: "))

    if op == "-":
        ans -= sn
    elif op == "x":
        ans *= sn
    elif op == "/":
        ans/= sn
    elif op == "+":
        ans += sn
    else:
        print("invalid operator")
    
print("result = ", ans)