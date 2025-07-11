numone = int(input("Tell me a number: "))
numtwo = int(input("Tell me another: "))
operation = input("What operation do you want? (* / + -) ")

if operation == "*":
    print(numone * numtwo)
elif operation == "/":
    print(numone / numtwo)
elif operation == "+":
    print(numone + numtwo)
elif operation == "-":
    print(numone - numtwo)