###### Python in a program to do the work with the argument's all the properties in the vs code
#### Postional Only Argument- \,new_Parameter
### Keyword Only Argument - new_parameter, * 
##### Let's do the Exersise what need in the Code 
#### ---------------------------------------------
### Postion Only Argument: 
def intro(name,/):
    print(f"My name is {name}")
### Calling the Function 
intro("Subin")
intro("Pawan Jung Rana")
#### Keyword Only Argument 

def intro(*,name):
    print(f"My name is {name}")
### Calling the Function: 

### Smart Calculator
# Create a function called smart_calc(a, b, /, *, operation="add") that:

# Takes two positional-only numbers (a, b)

# Accepts a keyword-only argument operation

# Returns the result based on operation type:

# "add" → addition

# "sub" → subtraction

# "mul" → multiplication

# "div" → division
### 3) Challenge 4: Student Grade Function
# Problem:

# Create a function called student_grade(name, marks, grade="A") that:

# Accepts a student’s name and marks

# Has a default parameter grade = "A"

# Prints the student’s details in the following format: