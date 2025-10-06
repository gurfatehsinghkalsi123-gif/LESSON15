def multiply(p, q):
    return p*q
def add(t,y):
    return t+y
def subtract(w, e):
    return w-e
def divide(a, b):
    return a/b

print(" Select an operator")
choice = int(input("1.addition\n2.subtract\n3.division\n4.multiplication"))
n1 = int(input("enter your first num"))
n2 = int(input("enter your second number"))
if choice == 1:
    print(add(n1, n2))
if choice == 2:
    print(subtract(n1, n2))
if choice == 3:
    print(divide(n1, n2))
if choice == 4:
    print(multiply(n1, n2))
