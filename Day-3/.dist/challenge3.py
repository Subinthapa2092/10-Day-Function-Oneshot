# . A stock price is **Rs. 480** today. 
# It increases by **6%** .

# Write a function using the **math module** to calculate the
# **new stock price** .

# stock_price = 480 
# rate = 6 
# ### Without Using Pow Function::
# def stock_calculation(price,increase):
#     result = price + price * increase/100
#     return result 
# print(stock_calculation(stock_price,rate))
### With using Math Module 
import math
stock_price = 480 
rate = 6 
### Without Using Pow Function::
def stock_calculation(price,increase):
    result = price*math.pow((1+increase/100),1) ### 1.06
    return result 
print(stock_calculation(stock_price,rate))