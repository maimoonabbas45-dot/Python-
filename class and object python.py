

class student :
    def __init__(self,name,age):       #constructor, self represent the current object  of class
        self.name = name               #instance variable
        self.age = age                
    def display(self) :             # method to show details
        print("name:", self.name)
        print("age:", self.age)

# create object outside the class
s1 = student("abc",22)
s1.display()

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start(self):
        print(self.model, "started")
       

car1 = Car("Red", "Audi")
car2 = Car("Blue", "BMW")

car1.start()   # Audi started
car2.start()   # BMW started


class student:
    name = "shb"
    rollno = 18
# create object of the class
student1 = student()

print(student1.name)
print(student1.rollno)

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

# create object
student1 = Student("Riya", 12)

print(student1.name)
print(student1.rollno)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)


   

class Student:
    # Class Attribute
    school  = "ABC School"

    def __init__(self, name, age):
        # Instance (Data) Attributes
        self.name = name
        self.age = age

# Create two objects
s1 = Student("Riya", 20)
s2 = Student("Amit", 22)

# Access class attribute
print(s1.school)   # ABC School

print(s1.name,s1.age)   # Access data attributes
print(s2.name,s2.age)
# Change class attribute
#student.school = "XYZ school"
#print(s1.school)   #xyz school
#print(s2.school)   #xyz school
s1.age =25
print(s1.age)

