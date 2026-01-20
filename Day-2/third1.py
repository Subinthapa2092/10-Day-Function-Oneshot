##### Keyword Argument's 
#### Normal Argumention: 
def myfunction(name,address):
    print(f"My name is {name}")
    print(f"My address is {address}")

myfunction("Dhading","Subin Thapa")

### Keyword Argument syntax: key(Parameter) = value(argument) 
### Reusable: and Same Order: 
def my_details(name, address):
    print(f"My name is {name}")
    print(f"My address is {address}")
my_details(address= "Kathmandu",name = "Subin Thapa")