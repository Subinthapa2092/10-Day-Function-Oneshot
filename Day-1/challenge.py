# 1. Write a function that **takes two 
# numbers** as input and **returns their sum**.
# - Test your function with different numbers.
# - Try calling it multiple times.

def calculation_sum(a,b):
    sum = a+b 
    return sum

print(calculation_sum(8,9))
print(calculation_sum(100,200))
## 2) 
# 1. Write a Python program to create a **simple calculator**
# using a function.
# - Ask the user to enter **two numbers**.
# - Ask the user to choose an operation — addition, subtraction, 
# multiplication, division, or power.
# - Use a **function** to perform the selected operation.
# - Display the result to the user.
# #### Simple Calculator: 

def Simple_calculator(number1,number2,option):
    if option == "+":
        result = number1 + number2
        return f"The sum of the number is {result}"
    elif option == "-":
        result = number1 - number2
        return f"The difference of the number is {result}" 
    elif option == "*":
        result = number1*number2 
        return f"The multiply of the number is {result}"
    elif option == "/":
        if number2 != 0:
            result = number1 /number2
            return f"The division of the number is {result}" 
        else:
            return f"Error not divisble by {number2}"
    else:
        return "Invalid Option : Check again and type"
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
option = input("Enter any option(+,-,*,/): ")
result = Simple_calculator(a,b,option)
print(result)

# ### Write a Python program to check whether a 
# number is prime or not using a function.
### Prime Number or Not 

def is_check():
    number = int(input("Enter any number: "))
    if number <= 1:
        print(f"The {number} is not a prime number")
    else:
        for i in range(2,int(number**0.5)+1):
            if i %2 == 0:
                print(f"The {number} is not a prime number")
                return False 
        print(f"The {number} is Prime")
        return True 

is_check()