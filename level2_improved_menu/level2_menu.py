print("---- LEVEL 2: IMPROVED MENU CALCULATOR ----")

while True: 
    try:
        print("\nSelect an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1–5): "))

        # Exit option
        if choice == 5:
            print("Thank you for using the calculator!")
            break

        # Invalid choice
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        # Inputs for operations
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

    except ValueError:
        print("Error: Please enter numeric values only.")
        continue

    else:
        # Operations (run only when no error occurs)
        if choice == 1:
            print(f"Result: {a + b}")
        elif choice == 2:
            print(f"Result: {a - b}")
        elif choice == 3:
            print(f"Result: {a * b}")
        elif choice == 4:
            try:
                print(f"Result: {a / b}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

    finally:
        print("Operation complete.")
