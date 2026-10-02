class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

if __name__ == "__main__":
    print("Welcome to the Calculator!")
    calc = Calculator()

    while True:
        print("\nChoose an option:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("Exiting the calculator...")
            break

        if choice in (1, 2, 3, 4):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number entered! Please try again.")
                continue

            if choice == 1:
                result = calc.addition(num1, num2)
            elif choice == 2:
                result = calc.subtraction(num1, num2)
            elif choice == 3:
                result = calc.multiplication(num1, num2)
            elif choice == 4:
                result = calc.division(num1, num2)

            print("Result:", result)
        else:
            print("Invalid choice. Please try again.")
