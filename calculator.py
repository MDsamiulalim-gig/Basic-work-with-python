def calculator():
    print("Simple calculator")
    print("Operation:+ - * /")

    while True:
        num1 = float(input("Enter First Number :"))
        operator = input("Enter Operator (+ - * /): ")
        num2 = float(input("Enter second Number :"))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero!")
                continue
        else:
            print("Invalid Operator")
            continue

        print("Result :", result)

        again = input("Do you want to continue? (Yes or No): ")
        if again.lower() != "yes":
            print("Goodbye!")
            break
calculator()