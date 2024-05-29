"""
> Python Class and Object :
A class is a blueprint or a template for creating objects, providing initial values for state
(member variable or attributes), and implementation of behavir (member function or
methods). The user-defined objects are created using the class keyword.

> Creating a class:
Let us now create a class using class keyword

Example:

class person:
    #default values
    name="Manasvi"
    age=9
    std=3

-----------------------------------------------------------------------------------------------------------------------------------------------


> Creating an object:
Object is the instance of the class used to access the properties of the class
Now lets creats an object of the class

Example:
obj1=person()


-----------------------------------------------------------------------------------------------------------------------------------------------
> Self Parameter:

The self parameter is a reference to the current instance of the class , and is used to access variable 
that belongs to the class.

it must be provided as the extra parameter inside the method defination.
-----------------------------------------------------------------------------------------------------------------------------------------------


"""

# Creating Class

class person:
    #default values
    name="Manasvi"
    age=9
    std=3

    def  info(self):
        print(f"My name is {self.name} , age is {self.age} and in the std {self.std}")


a=person()

a. name="Aditya"
a.age=22
a.std=15

b=person()

b.name="Bhushan"
b.age=21
b.std=14


a.info()
b.info()