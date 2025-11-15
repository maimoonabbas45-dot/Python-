#public member
class Employee:
    def __init__(self, name):
        self.name = name   # public variable

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # can access method
# print(emp.name)      # can access variable

#protected  memeber
class employee:
    def __init__(self, name,age):
        self._name = name  #protected variable
        self._age = age    #protected variable
    def _display_info(self) :    #protcted method
        print (f"name:{self._name},age :{self._age}")

class manager(employee):
    def show(self):
        self._display_info()   # Can access protected method from parent class
        
#create object outside the class
emp = employee("ali",45)
mgr = manager("hussain",20)
mgr.show()


#private member
class Employee:
    def __init__(self,name,salary):
        self.name = name #public any one can access
        self.__salary = salary #private cannot access directly

    def show__salary(self): 
        print(self.__salary) #access private safely

emp = Employee("rahul",50000)
print(emp.name)        #works, prints the name
emp.show__salary         #works,print the salary
emp.show__salary()
#print(emp.salary) #it will show error because we can't access private variable

# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    # method to get name
    def getName(self):
        return self.name

    # method to check if person is employee
    def isEmployee(self):
        return False


# Child class (inherits from Person)
class Employee(Person):
    # overriding the method
    def isEmployee(self):
        return True


# Object of Person class
emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())  # Output: Geek1 False

# Object of Employee class
emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())  # Output: Geek2 True
