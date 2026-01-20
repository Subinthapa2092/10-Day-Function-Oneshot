# 2. A rectangle has a length of 12.5 units and a 
# width of 7.8 units. Write a Python program to calculate :
# - The area of the rectangle
# - The perimeter of the rectangle
# - The diagonal of the rectangle (use math.sqrt).
import math
length = 12.5 
width = 7.8

def math_calculation(l,b):
    area = l*b
    print(f"The area of rectangle is {area}")
    perimeter = 2*(l+b)
    print(f"The perimeter of the rectangle is {perimeter}")
    diagonal = math.sqrt(l**2 +b**2) ### h^2 = l^2+b^2
    print(f"The diagonal of the rectangle is {diagonal}")
math_calculation(length,width)