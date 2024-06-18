"""
> Access Specifiers / Modifiers

Access specifiers or access modifiers in python programming are used to limit the access of class
variable and class methods outside of class while implementing the concepts of inheritance.

> Types of access specifiers

1. Public access modifier 
2. Private access modifier
3. Protected access modifier

----------------------------------------------------------------------------------------------------------------

> Public Access Specifier in Python

All the varialbe and methods (member function )in python are by default public. Any instance variable in
a class followed by the 'self' keyword ie. self.var_ name are public accessed.


Example:

class student:

    def __init__(self,age,name):

        self.age=age  #public variable
        self.name=name #public variable


obj=student(22,'adii')

print(obj.name)
print(obj.age)

----------------------------------------------------------------------------------------------------------------------------
> Private Access Modifier

In python, there is no strict concept of "private" acess modifiers like in some other Programming language.
method should be considered private by prefixing its name with a double underscore (__) .
This is known as a "Weak internal use indicator" and it is convesion only.not strict rule


Example:

class student:

    def __init__(self) :
        self.__name= "aditya"  # making private attributes


a=student()
# print(a.__name) # 'student' object has no attribute '__name'

print(a._student__name) # Now you can access the variable 



> Name mangling:

Name mangling in Python is a technique used to protect class-private and superclass-private atributes form being accidentallly overwritten
by subclass.
Name of class-private and superclass-private attributes are transformed by the addittion of a single leading underscore and 
a double leading underscore respectively.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
> Protected Access Modifier

its improtant to note that the single underscope is just a naming convention , and does not acctually provide any protecton 
or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by 
a single underscore (_) i.e _varName.

example:

class student:

    def __init__(self) :
        self.__name= "aditya"


a=student()
"""


class student:

    def __init__(self) :
        self.__name= "aditya"


a=student()
# print(a.__name) # 'student' object has no attribute '__name'

print(a._student__name) # Now you can access the variable 

# print(a.__dir__()) mehtods you can apply on a 