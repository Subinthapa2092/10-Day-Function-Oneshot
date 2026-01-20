# 1. Create a function that **accepts a
# person’s name and age** (with default age = 18) 
# and prints:

# ```python
# Name: <name>, Age: <age>
# ```

# - Call it **with and without passing the age**.

# def Person(name,age = 18):
#     print("Name:",name,"Age:",age)

# # Person("Subin Thapa",17)
# Person("Aayush Pokhrel")

# Create a function student_report that accepts:
# name (string)
# marks (integer)
# grade (string, default = "A")
# The function should print:
# Name: <name>
# Marks: <marks>
# Grade: <grade>
# ​
# Task:
# Call it with all three arguments
# Call it with only name and marks 
# (use default grade)

# def student_report(name,marks,grade = "A"):
#     print("Name:",name)
#     print("Marks:",marks)
#     print("Grade:",grade)
# student_report("Amor Bhatta",90,"A+")
# student_report("Subin Thapa",81)
# student_report("Yubraj Pandey",31,"Fail")
# student_report("Saubhagya",67,"B")





























# Create a function employee_info that accepts:

# name (string, positional-only)
# department (string, keyword-only)
# salary (integer, default = 30000)
# The function should print
# Employee: <name>
# Department: <department>
# Salary: <salary>
# ​
# Task:
# Call it correctly using positional-only and keyword-only arguments
# Call it again using default salary
# Try swapping the order incorrectly to see what error occurs
def employee_details(name,/,*,department,salary = 30000):
    print(f"Employee Name: {name}")
    print(f"Department: {department}")
    print(f"Salary : {salary}")
employee_details("Subin Thapa",department ="Data Science")
employee_details("Kaushal Sapkota",department="Sport",salary = "5 lakh")