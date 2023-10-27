 # ============Simple Calculator========== 
print("Select an operation to Perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = int(input())
if operation == 1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The sum is ",(num1+num2))
    
elif operation == 2:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The Subtract is ",(num1 - num2))
    
elif operation == 3:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The Multiply is ",num1*num2)
    
elif operation == 4:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The Division is ",num1/num2)
    
else:
    print("Invalid Entry")