num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+,-,*,/): ")
if operation == '+':
    results = num1+num2
elif operation == '-':
    results = num1-num2
elif operation == '*':
    results = num1*num2
elif operation == '/':
    if num2 == 0:
        print("Error! division by zero is invalid")
        exit()
    results = num1/num2
else:
    print("Invalid operation!")
    exit()
print(f"{num1} {operation} {num2} = {results}")
