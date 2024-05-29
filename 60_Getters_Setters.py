"""
> Getters :

Getters in Python are methods that are used to access the values of an object's properties . They are used to return the value of a 
specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

Example:


class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")    

    @property #property decorators getters
    def Tenx_value(self):
        return 10 * self._value


obj= Myclass(10)

obj.show() # Value is 10
print(obj._value) # 10

print(obj.Tenx_value) #100

==========================================================================================================================================================


> Setters

it is important to note that the getters do not take any parameters and we cannot set
value through getter method . for that we need setter method which can be added by decorting method
@property_name.setter

Example:

class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")    

    @property #property decorators getters
    def Tenx_value(self):
        pass

    @Tenx_value.setter
    def Tenx_value(self,new_value):
        self._value=new_value/10

        
obj= Myclass(10)

print(obj._value) # 10

obj.Tenx_value=67
obj.show() # value is 6.7

==========================================================================================================================================================

"""


class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")    

    @property #property decorators getters
    def Tenx_value(self):
        pass
        # return 10 * self._value

    @Tenx_value.setter
    def Tenx_value(self,new_value):
        self._value=new_value/10


obj= Myclass(10)

# obj.show() # Value is 10
print(obj._value) # 10

# print(obj.Tenx_value) #100

obj.Tenx_value=67
obj.show() # value is 6.7
