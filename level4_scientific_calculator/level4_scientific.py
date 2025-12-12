# level4_scientific.py
import math

def safe_float(prompt):
    """Get a float from the user or raise ValueError."""
    return float(input(prompt))

def nth_root(x, n):
    """Return the n-th root. Supports odd roots of negative numbers."""
    if n == 0:
        raise ValueError("Root degree cannot be zero.")
    # If x is negative and n is odd, allow negative result
    if x < 0 and n % 2 == 1:
        return - (abs(x) ** (1.0 / n))
    elif x < 0:
        raise ValueError("Even root of negative number is not allowed.")
    else:
        return x ** (1.0 / n)

print("---- LEVEL 4: SCIENTIFIC CALCULATOR ----")

while True:
    try:
        print("\nSelect an option:")
        print("1. Trigonometric functions (sin, cos, tan)")
        print("2. Inverse trigonometric functions (asin, acos, atan)")
        print("3. Logarithms (ln, log10)")
        print("4. Exponential (e^x) and power")
        print("5. Factorial")
        print("6. N-th root")
        print("7. Absolute value")
        print("8. Convert degrees <-> radians")
        print("9. Back to main / Exit")
        
        choice = int(input("Enter your choice (1–9): "))

        if choice == 9:
            print("Thank you for using the scientific calculator!")
            break

        # ---- TRIG (choice 1) ----
        if choice == 1:
            # Ask for degrees or radians
            unit = input("Are your angles in degrees? (y/n): ").strip().lower()
            angle = safe_float("Enter the angle: ")
            if unit == 'y':
                angle = math.radians(angle)

            print("Choose function: 1) sin  2) cos  3) tan")
            fn = int(input("Enter 1, 2 or 3: "))
            if fn == 1:
                print(f"sin = {math.sin(angle)}")
            elif fn == 2:
                print(f"cos = {math.cos(angle)}")
            elif fn == 3:
                try:
                    print(f"tan = {math.tan(angle)}")
                except Exception as e:
                    print("Error computing tan:", e)
            else:
                print("Invalid selection for trig function.")

        # ---- INVERSE TRIG (choice 2) ----
        elif choice == 2:
            print("Choose function: 1) asin  2) acos  3) atan")
            fn = int(input("Enter 1, 2 or 3: "))
            x = safe_float("Enter the value (domain dependent): ")
            try:
                if fn == 1:
                    res = math.asin(x)
                elif fn == 2:
                    res = math.acos(x)
                elif fn == 3:
                    res = math.atan(x)
                else:
                    print("Invalid selection for inverse trig.")
                    continue

                unit = input("Do you want result in degrees? (y/n): ").strip().lower()
                if unit == 'y':
                    res = math.degrees(res)
                print(f"Result = {res}")
            except ValueError:
                print("Math domain error for the given input (e.g., asin/acos require -1<=x<=1).")

        # ---- LOGARITHMS (choice 3) ----
        elif choice == 3:
            print("Choose: 1) ln (natural log)  2) log10 (base-10)")
            fn = int(input("Enter 1 or 2: "))
            x = safe_float("Enter a positive number: ")
            if x <= 0:
                print("Error: Logarithm undefined for non-positive numbers.")
                continue
            if fn == 1:
                print(f"ln({x}) = {math.log(x)}")
            elif fn == 2:
                print(f"log10({x}) = {math.log10(x)}")
            else:
                print("Invalid selection for logarithm.")

        # ---- EXPONENTIAL & POWER (choice 4) ----
        elif choice == 4:
            print("1) e^x (exponential)  2) power a^b")
            fn = int(input("Enter 1 or 2: "))
            if fn == 1:
                x = safe_float("Enter x: ")
                print(f"e^{x} = {math.exp(x)}")
            elif fn == 2:
                a = safe_float("Enter base a: ")
                b = safe_float("Enter exponent b: ")
                print(f"{a}^{b} = {a ** b}")
            else:
                print("Invalid selection for exponential/power.")

        # ---- FACTORIAL (choice 5) ----
        elif choice == 5:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Error: Factorial for negative numbers not defined.")
            else:
                try:
                    print(f"{n}! = {math.factorial(n)}")
                except ValueError:
                    print("Error: factorial input must be an integer >= 0.")

        # ---- N-th ROOT (choice 6) ----
        elif choice == 6:
            x = float(input("Enter the number (x): "))
            n = int(input("Enter the root degree (n): "))
            try:
                root = nth_root(x, n)
                print(f"{n}-th root of {x} = {root}")
            except ValueError as ve:
                print("Error:", ve)

        # ---- ABSOLUTE (choice 7) ----
        elif choice == 7:
            x = float(input("Enter the number: "))
            print(f"abs({x}) = {abs(x)}")

        # ---- DEGREE / RADIAN CONVERSION (choice 8) ----
        elif choice == 8:
            print("1) Degrees -> Radians  2) Radians -> Degrees")
            fn = int(input("Enter 1 or 2: "))
            if fn == 1:
                d = float(input("Enter degrees: "))
                print(f"{d} degrees = {math.radians(d)} radians")
            elif fn == 2:
                r = float(input("Enter radians: "))
                print(f"{r} radians = {math.degrees(r)} degrees")
            else:
                print("Invalid selection for conversion.")

        else:
            print("Invalid choice. Enter a number between 1 and 9.")

    except ValueError:
        print("Error: Please enter valid numeric values and valid menu choices.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Operation complete.")
