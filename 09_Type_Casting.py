'''
Typecasting in python


the conversion of one data type into the other data type is known as type casting in python
or type conversion in python.


python supports a wide variety of function or methods like:
int(),float(), str(), hex(),oct(),tuple(),set(),list(),dict(),etc
for the type casting in python.


Two Types of Typecasting:
1.Explict Conversion (Explicit type casting in python)
2.Implicit Conversion (Implicit type casting in python)

-------------------------------------------------------------------------------------------------

#Explicit typecasting: 

The conversion of one data type into anthor data type, done via developer or programmer's intervention or 
manually as per the requirment , is known as explicit type conversion

It can be achieved with the help of Python's built-in-type conversion function such as 
int(), float(),hex(),oct(),str(),etc.

Example explicit typecasting:

string="15"

num=7

string_number=int(string) #throws an error if string is not valid integer

print(string_number+num)

-------------------------------------------------------------------------------------------------
#Implicit type Casting:

Data types in Python do not have the same level i.e. ordering of data type is not same in python
Some of the data types have higer-order,and same in Pyhton. Some of the data types have higher-order and 
some have lower order. While programming any operation on variables with different data types in python,one
of the variable's data types will be changed to the higher data types. According to the level, one data is converted into other
by the pyhton interpreter itself (automatically ) , This is called , implicit typeCasting in python


Python Converts a smaller data type to a higher data type to prevent data loss

Example of Implicit type Casting:

a=7
print(type(a))  // int 

b=3.8
print(type(b))  // float


c= a+ b


print(c)  // float 

print(type(c))  // float


'''



string="15"

num=7

string_number=int(string) #throws an error if string is not valid integer

print(string_number+num)



#Implicit TypeCasting

c=1.9
d=8

print(c+d)