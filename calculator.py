num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")


choice= input("Enter operation (1,2,3,4): ")
result=None
match choice:
    case '1':
        result= num1 + num2
    
    case '2':
        result= num1 - num2
    case '3':
        result= num1 * num2
    case '4':
        if num2 !=0:
            result= num1 / num2
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid input")
            
print("Result: ", result)
    
