while True:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    operator = str(input("Choose an operator: (+,-,*,/)"))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2) 
    elif operator == "*":
        print("Result:", num1 * num2) 
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else: 
            print("Result:", num1 / num2)
    else: 
        print("Invalid Operator choosen.")

    again = input("Do you want to calculate again? (yes/no):").lower()
    if again != "yes":
        print("Goodbye!")
        break 

