''' Statement : If the user enters the following values the o/p will be given : 45 * 3 = 555, 56 + 9 = 77
56 / 6 = 4. Design a calculator which will solve all the values correctly except this .
i/p : The program should take operator and two numbers as an i/p from the user and then return the result.  '''


from sys import *


def repeat():           # if we want to continue the calculation
    a = 1
    while a == 1:
        ip = int(input("Do want to calculate again ? If yes, press 1 else press 2:"))
        if ip == 2:
            break
        # ip1 = ip.capitalize()
        elif ip == 1:
            print("!!!!! Welcome to Anindya's calculator !!!!!\nPress '+' for Addition\nPress '-' for Subtraction\nPress '*' for Multiplication\nPress '/' for Division\nPress '**' for power\nPress '%' for Modulus")
            op = input("Enter the operator:")
            x = int(input("Enter the 1st value:"))
            y = int(input("Enter the 2nd value:"))
            z1 = calculator(x, y, op)
            print(z1)
    sys.exit("Thank You")


def calculator(x, y, op):       # op = operator, x = 1st element, y = 2nd element

    # for faulty statements

    if x == 45 and y == 3 and op == '*':
        return 555
    elif x == 56 and y == 9 and op == '+':
        return 77
    elif x == 56 and y == 9 and op == '/':
        return 4

    # for correct calculations
    elif op == '+':         # Addition
        return x + y
    elif op == '-':         # Subtraction
        return x - y
    elif op == '*':         # Multiplication
        return x * y
    elif op == '/':         # Division
        if y == 0 or y < 0:     # if the denominator is zero or -ve number we can't divide
            print("Can't Divide by", y)
            # exit()
        return x / y            # if the denominator is -ve number performing the Division
    elif op == '**':            # Power
        return x ** y
    elif op == '%':             # Modulus
        return x % y
    else:
        print("!!! Wrong Input !!! Plz Try Again")




print("!!!!! Welcome to Anindya's calculator !!!!!\nPress '+' for Addition\nPress '-' for Subtraction\nPress '*' for Multiplication\nPress '/' for Division\nPress '**' for power\nPress '%' for Modulus")
op = input("Enter the operator:")           # taking the operator as user i/p
if op != '+' and op != '-' and op != '/' and op != '*' and op != '**' and op != '%':    # checking for correct operator
    sys.exit("!!! Wrong Input !!! Plz Try Again")
else:
    x = int(input("Enter the 1st value:"))      # 1st element
    y = int(input("Enter the 2nd value:"))      # 2nd element
    z = calculator(x, y, op)    # calling the calculator
    print(z)                    # printing the value
    repeat()                    # if we want to calculate again

