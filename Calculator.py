import math
def show_menu():
    print("\n" + "=" * 40)
    print(" ADVANCED CALCULATOR")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Modulus (%)")
    print("7. Power (**)")
    print("8. Square Root (sqrt)")
    print("9. Absolute Value (abs)")
    print("10. Factorial (!)")
    print("11. Logarithm (log)")
    print("12. Sine (sin)")
    print("13. Cosine (cos)")
    print("14. Tangent (tan)")
    print("15. Percentage")
    print("0. Exit")
    print("=" * 40)
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
def calculate():
    while True:
        show_menu()
        choice = input("Choose an operation: ").strip()
        if choice == "0":
            print("Calculator closed. Goodbye!")
            break
        if choice in ["1", "2", "3", "4", "5", "6", "7", "15"]:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            if choice == "1":
                result = num1 + num2
            elif choice == "2":
                result = num1 - num2
            elif choice == "3":
                result = num1 * num2
            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            elif choice == "5":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 // num2
            elif choice == "6":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 % num2
            elif choice == "7":
                try:
                    result = num1 ** num2
                except OverflowError:
                    print("Error: Result is too large.")
                    continue
            elif choice == "15":
                result = (num1 * num2) / 100
        elif choice in ["8", "9", "10", "11", "12", "13", "14"]:
            num = get_number("Enter a number: ")
            if choice == "8":
                if num < 0:
                    print("Error: Square root of a negative number is not real.")
                    continue
                result = math.sqrt(num)
            elif choice == "9":
                result = abs(num)
            elif choice == "10":
                if num < 0 or not num.is_integer():
                    print("Error: Factorial requires a non-negative integer.")
                    continue
                result = math.factorial(int(num))
            elif choice == "11":
                if num <= 0:
                    print("Error: Logarithm requires a positive number.")
                    continue
                result = math.log10(num)
            elif choice == "12":
                result = math.sin(math.radians(num))
            elif choice == "13":
                result = math.cos(math.radians(num))
            elif choice == "14":
                if num % 180 == 90:
                    print("Error: Tangent is undefined for this angle.")
                    continue
                result = math.tan(math.radians(num))
        else:
            print("Invalid choice! Please select an option from the menu.")
            continue
        print("-" * 40)
        print(f"Result: {result:g}")
        print("-" * 40)
if __name__ == "__main__":
    calculate()