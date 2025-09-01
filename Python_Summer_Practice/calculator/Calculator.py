# Simple Calculator

numone = int(input("Tell me a number: "))
numtwo = int(input("Tell me another: "))
operation = input("What operation do you want? (* / + -) ")

if operation == "*":
    print(numone * numtwo)
elif operation == "/":
    if numtwo == 0:
        print("Error: Division by zero is not allowed.")
        numtwo = int(input("Please enter a non-zero number: "))
        print(numone / numtwo)
    print(numone / numtwo)
elif operation == "+":
    print(numone + numtwo)
elif operation == "-":
    print(numone - numtwo)