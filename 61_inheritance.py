"""
> Inhertance in python:

When a clas derives form another class. The child class will inherit all the public and protected properties
and method from the parent class. In Addition, it can have its own properties and methods, this is called as inheritance.

> Types of Inheritance:

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierachical Inheritance
5. Hybrid Inheritance


"""


# > Python Inheritance syntax:


class Employee:

    def __init__(self,name,id) :
        self.name=name
        self.id=id
    
    def ShowDetails(self):
        print(f"The name of Employee {self.id} is {self.name}")


class programmer(Employee):

    def ShowLang(self):
        print("The default language is Python")

a1=Employee("Aditya",1109)

a1.ShowDetails() # The name of Employee 1109 is Aditya

a2=programmer("Manasvi",245)

a2.ShowDetails()
#   The name of Employee 245 is Manasvi
a2.ShowLang()
#   The default language is Python