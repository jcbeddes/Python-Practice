def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input("What operation do you want? (+, -, *, /) ")
        if op in valid_operations:
            return op
        else:
            print("Invalid operation. Try again.")

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: cannot divide by zero."
        return num1 / num2


def main():
    num1 = get_number("Tell me a number: ")
    num2 = get_number("Tell me another: ")
    operation = get_operation()
    result = calculate(num1, num2, operation)
    print("Result:", result)

main()