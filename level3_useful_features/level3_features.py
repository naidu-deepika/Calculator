import math

print("---- LEVEL 3: USEFUL FEATURES CALCULATOR ----")

while True:
    try:
        print("\nSelect an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage (X% of Y)")
        print("6. Square (x²)")
        print("7. Cube (x³)")
        print("8. Power (a^b)")
        print("9. Square Root (√x)")
        print("10. Modulus (a % b)")
        print("11. Average of N numbers")
        print("12. Exit")

        choice = int(input("Enter your choice (1–12): "))

        if choice == 12:
            print("Thank you for using the calculator!")
            break

        # ---------------- BASIC OPERATIONS ----------------
        if choice in [1, 2, 3, 4, 10]:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

        # ---------------- SINGLE INPUT FUNCTIONS ----------------
        elif choice in [6, 7, 9]:
            x = float(input("Enter the number: "))

        # ---------------- POWER FUNCTION ----------------
        elif choice == 8:
            a = float(input("Enter the base (a): "))
            b = float(input("Enter the exponent (b): "))

        # ---------------- PERCENTAGE FUNCTION ----------------
        elif choice == 5:
            x = float(input("Enter X: "))
            y = float(input("Enter Y: "))

        # ---------------- AVERAGE FUNCTION ----------------
        elif choice == 11:
            n = int(input("How many numbers? "))
            numbers = []
            for i in range(n):
                val = float(input(f"Enter number {i+1}: "))
                numbers.append(val)

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")
            continue

    except ValueError:
        print("Error: Please enter valid numeric values.")
        continue

    # -------------- PERFORM OPERATIONS ----------------
    else:
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
                print("Error: Cannot divide by zero.")
        elif choice == 5:
            print(f"Result: {(x / 100) * y}")
        elif choice == 6:
            print(f"Square: {x ** 2}")
        elif choice == 7:
            print(f"Cube: {x ** 3}")
        elif choice == 8:
            print(f"Result: {a ** b}")
        elif choice == 9:
            if x < 0:
                print("Error: Square root of negative number is not allowed.")
            else:
                print(f"Square Root: {math.sqrt(x)}")
        elif choice == 10:
            print(f"Result: {a % b}")
        elif choice == 11:
            print(f"Average: {sum(numbers) / len(numbers)}")

    finally:
        print("Operation complete.")
