try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("What kind of operation do you want to perform.Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")
    o = input("Enter the operation: ")

except ValueError:
    print("Invalid input. Enter numbers only.")

else:
    # Runs only if no exception in try
    match o:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            try:
                print(a / b)
            except ZeroDivisionError:
                print("You cannot divide by zero.")
        case _:
            print("Invalid operation.")

finally:
    print("Thank you for using the calculator!")

