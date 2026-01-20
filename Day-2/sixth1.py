#### 
#### Passing List Data Structure or Data type: 

# my_fruit = {"Apple","Banana","Orange","Pineapple"}

# def details_list(fruit):
#     for i in fruit:
#       print(i)

# details_list(my_fruit)
### Passing the student details in the form of the dictionary: 

my_details = {'name': "Subin Thapa",'age':18,'class':"Bachelor in Data Science"}

def details(my_details):
    print(f"Name:{my_details['name']},Age:{my_details['age']},Class:{my_details['class']}")
    print(my_details)

details(my_details)