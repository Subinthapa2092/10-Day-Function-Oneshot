### Positional Only Argument  and Keyword Only Argument: 

# def myfunction(a,b,/,*,c,d):
#     return a+b+c+d
# x = myfunction(10,30,c = 30,50)
# print(x)
# print(myfunction(30,40, c = 90,d = 100))
### After positonal Only Argument: 

def myfunction(a,b,/,d):
    print(a+b+d)
myfunction(10,20,90)