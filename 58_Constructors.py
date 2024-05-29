"""
> Constructors:

A constructors is a special method in a class used to create and initialize  an object of a class. there are different 
types of constructors . Constructors is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automaticallly when an object is created of a class. The main
purpose of a constructors is to initialize or assign values to the data members of that class . It cannot return any
values other than none

-------------------------------------------------------------------------------------------------------------------------------------

Syntax of Python Costructor:

 def __init__(self,name,occ) :
    #initializations
    
init is one of the reserved function in python . In Object Oriented Programming , it is known as
constructor.


----------------------------------------------------------------------------------------------------------------------------------------

Types of Constructors in Python:

1. Parameterized constructor
2. Default Constructor


> Parameterized constructor in PYthon:
When the constructor accepts arguments along with self, it is know as parameterized
constructor.

These agruments can be used inside the class to assign the value to the data members.

Example:


class person:

    def __init__(self,name,occ) :

        self.name=name
        self.occ=occ
        print("hey i am person")

     def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("adii","data-scientist")
b= person("balavant","chinces-vala")
        

a.info()
b.info()


Output:

hey i am person
hey i am person
adii is a data-scientist
balavant is a chinces-vala

---------------------------------------------------------------------------------------------------
> Default Constructor in Python:

 When the constructor does't accept any arguments from the object and has only one argument , self, in the
 constructor it is knows as a default constructor.

Example:
    class details:
    def __init__(self) :
        print("animal crab belongs to crustaceans group")
    
obj1=details()


OUtput:
animal crab belongs to crustaceans group
"""

class person:

    def __init__(self,name,occ) :

        self.name=name
        self.occ=occ
        print("hey i am person")
        

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("adii","data-scientist")
b= person("balavant","chinces-vala")
        

a.info()
b.info

class details:
    def __init__(self) :
        print("animal crab belongs to crustaceans group")
    
obj1=details()

