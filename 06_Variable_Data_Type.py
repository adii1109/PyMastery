'''

What is a variable ?


variable is a container that holds data. Very Similar to how our containers holds sugar, salts etc
Creating a variable is like creating a placeholder in memory and assigninig it some value. In Python 
its as Writing 
'''

a=1
b= True
c="harry"
d=None

print("Here Type of all data type : ")

print (type(a)) # Number 
print (type(b)) # bollean 
print (type(c)) # Stirng
print (type(d)) # 


'''
What is Data Type ?

Data type specifies the type of value a variable holds. This is required in programming to do various operation without causing an 
error.

In python, we can print the type of any operator using type Function :


1. Numeric Data. Int , float , complex

# int : 3, -8 , 0

#float : 7.348, -8.2, 0.0001

# Complex : 6 + 7i


2. Text data : String

string : "Hello Adii", "Python Programming"

3.Boolean Data :

Boolean data consists of value True or False.

4. Sequenced data : list, tuple

# list :
A list is an ordered collection of data with elements separated by a comma and enclosed within squre brackets.
List are mutable and can be modified after creation

list1=[8,2,3,[-4,5],["apple","banana"]]
print (list1);


#Tuple:
a tuple is an ordered collection of data with elements separeated by a comma and enclosed within parenthees. Tuples are immutable and
can not be modified after creation

tuple1=(("parrot","sparrow"),("Lion", "Tiger"))
print (tuple1)

5.Mapped data : dict 

dict : A dictionary is an unorded collection of data containing a Key: value pair. 
The key value pair are enclosed within curly brackets.


dict1={"name": "Aditya", "age":22, "CanVote": True}
print (dict1)
'''

print("here list : ")
list1=[8,2,3,[-4,5],["apple","banana"]]
print (list1);

print ("\n")
print("here tuple : \n")
tuple1=(("parrot","sparrow"),("Lion", "Tiger"))
print (tuple1)

print ("\n")
print("here dictionary : \n")

dict1={"name": "Aditya", "age":22, "CanVote": True}
print (dict1)