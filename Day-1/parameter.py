#### Python in a program to do or work with parameter and Return type: 

## No parameter , No return type 

## Sum of Number: 
## Defining the Function: 
def Addition():
    a = int(input("Enter the first number "))
    b = int(input("Enter the Second number: "))
    result = a+b 
    print(f"The sum of the number is {result}")
#### Calling now the function: 
Addition()
#2) No parameter with return type: 
### Function Defining: 
def addition():
    a = int(input("Enter any number1: "))
    b = int(input("Enter any number2: "))
    result = a+b 
    return result
### Function Calling
print(addition())

### Square of Number: 
### Parameter with no return type: 
## Function Defining: 
def square(number1):
    result = number1**2
    print(result)

### Function Calling:
a = int(input("Enter any a number: ")) 
square(a)
## Parameter and Return Type: 

def calculation_division(a,b):
    result = a/b
    return result 
number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number 2: "))
print(calculation_division(number1,number2))