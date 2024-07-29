a = int(input("Enter first number : "))
operator = input("Enter operator(+,-,*,/) : ")
b = int(input("Enter second number : "))

if(operator == '+'):
    print("Answer : ",a+b)
elif(operator == '-'):
    print("Answer : ",a-b)
elif(operator == '*'):
    print("Answer : ",a*b)
elif(operator == '/'):
    if(b != 0):
        print("Answer : ",a/b)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid operation")