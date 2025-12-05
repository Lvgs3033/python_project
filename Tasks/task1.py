import sys

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("\nError: Cannot divide by zero.")
        return None
    return n1 / n2

def get_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 5, 3.14).")
            return None

def main():
    print("--- Python CLI Calculator ---")

    while True:
        print("\nAvailable Operations:")
        print("  1. Add      (+)")
        print("  2. Subtract (-)")
        print("  3. Multiply (*)")
        print("  4. Divide   (/)")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            sys.exit(0)

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        operations = {
            '1': ('Add', add),
            '2': ('Subtract', subtract),
            '3': ('Multiply', multiply),
            '4': ('Divide', divide)
        }

        op_name, op_func = operations[choice]

        num1 = get_number_input(f"Enter the first number for {op_name}: ")
        if num1 is None:
            continue

        num2 = get_number_input(f"Enter the second number for {op_name}: ")
        if num2 is None:
            continue

        result = op_func(num1, num2)

        if result is not None:
            print(f"\nResult: {num1} {operations[choice][0].lower()} {num2} = {result}")

        continue_prompt = input("Press Enter to continue, or type 'n' to exit: ").strip().lower()
        if continue_prompt == 'n':
            print("Exiting calculator. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()