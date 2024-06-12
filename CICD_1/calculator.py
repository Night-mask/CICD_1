import sys

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'

# Direct execution of the script
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <num2> <operation>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

result = calculator(num1, num2, operation)
print(f"Result: {result}")
