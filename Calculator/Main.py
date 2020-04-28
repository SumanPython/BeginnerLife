print("Welcome to the calculator Application")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("Q. Quit")

    choice = input("Please enter your choice ")
    if choice == "q" or choice == "Q":
        break

    print("Please enter two numbers")
    num1 = int(input("Please enter num1 "))
    num2 = int(input("Please enter num2 "))

    if choice == "1":
        from Addition import *
        addition(num1, num2)

    elif choice == "2":
        from Subtraction import *
        subtraction(num1, num2)

    elif choice == "3":
        from Multiplication import *
        multiplication(num1, num2)

    elif choice == "4":
        from Division import *
        division(num1, num2)

    elif choice == "5":
        from Modulo import *
        modulo(num1, num2)



