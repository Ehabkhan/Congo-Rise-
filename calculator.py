def calculator(num1,num2,operation):
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return num1-num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
          if num2!=0:
              return num1 / num2
          else:
              return ("Error, invalid value: " )
     
    else:
        return ("Error , Invalid operation: " )
    
    
num1=float(input("Enter first number : "))  
num2=float(input("Enter second number : "))  

operation = input("Enter operation to be performed (+,-,*,/)")

result = calculator (num1,num2,operation)
print("Result ", result)