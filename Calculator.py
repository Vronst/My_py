
def calculate():

    start = True

    while start:
        x = input("C: Calculate\tX: Exit\n").upper()
        if x == "C":
            calculator()
        elif x == "X":
            start = False
        else:
            print("Not an option\n")

def calculator():
    num = float(input("Type number: \n"))
    on = True
    while on:
        op = input("Choose operand:\n/\t*\n+\t-\t^\t^.\nx: exit\n")
        while op not in "+-/*^.x":
            print("Type proper operand!")
            op = input("Choose operand:\n/\t*\n+\t-\t^\nx: exit\n")
        if op == "x":
            on = False
        elif op == "+":
            num1 = float(input("Type second number:\n"))
            num += num1
            print(f"{num}\n")
        elif op == "-":
            num1 = float(input("Type second number:\n"))
            num -= num1
            print(f"{num}\n")
        elif op == "/":
            num1 = float(input("Type second number:\n"))
            num /= num1
            print(f"{num}\n")
        elif op == "*":
            num1 = float(input("Type second number:\n"))
            num *= num1
            print(f"{num}\n")
        elif op == "^.":
            num1 = float(input("Type second number:\n"))
            num = pow(num, num1)
            print(num)
        else:
            num1 = input("Type second number (musi byc caloscia!):\n")
            while num1 not in "1234567890":
                num1 = input("Type second number (musi byc caloscia!):\n")
            num1 = int(num1)
            result = 1
            for power in range(num1):
                result *= num
            print(f"{result}\n")




calculate()