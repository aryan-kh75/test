#calculator.py
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
def calculate(operation, x, y):
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation")
if __name__ == "__main__":
    print("Welcome to the calculator!")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        if operation == 'exit':
            print("Goodbye!")
            break
        x = float(input("Enter first number: ")) 
        y = float(input("Enter second number: "))
        try:
            result = calculate(operation, x, y)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)