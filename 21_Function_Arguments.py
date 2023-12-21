'''

Function Arguments and return Statement:

There are four types of arguments that we can provide in a function:

> Default Arguments
> Keyword Arguments
> Variable length Arguments
> Required Arguments


================================================================================================
Default arguments:

We can can provide a default value while creating a function . This way the function assumes a default value 
even if a value is not provided in the function call for that argument.


Example: 

def average(a=9,b=1):
    print((a+b)/2)


average(5,15)
average(5)
average(b=9)

Output:

10.0
3
9

======================================================================================

#Keyword arguments:

We can provide arguments with key = value, this way the interpreter recognizes the argumets by the
parameter name. Hence, the the order in which the arguments are passed does not matter


Example:

def average(a,b):
    print(a+b)

average(b=1,a=2) // order index not matter


====================================================================================

# Required arguments:

it case we dont pass the arguments with key = value syntax, then it is necessary to pass
the arguments in the correct positional order and the number of arguments passed should math with 
actual function definition..


Example1= When number of argumets passed does not match to the actual function defination

def name(fname,mname,lname):
    print("hello" , fname,mname,lname)

name("peter","quill")

Output:

name('peter','Quill");
TypeError: name() missing  1 required positional
argument:"lname"

Example2= With all argumets

def name(fname,mname,lname):
    print("hello" , fname,mname,lname)

name('aditya','shrikant','patil')

Output:

hello, aditya shrikant patil

======================================================================================
#Variable-length arguments:

Sometimes we may need to pass more arguments the those defined in the actual function . This can be done 
using variable-length arguments.


There are two ways to achieve this:

Arbitary Arguments:

While creating a function a *before the parameter the parameter name while defining the function
the function accesses the arguments by processing them in the from of tuple.


Example:

def average(*numbers):  #takes as a tuple

    sum=0

    for i in numbers:
        sum+=i
    
    print("Averge : ",sum/len(numbers))


average(1,2,3,4,5)


OUtput:

3.0

Example2:

def name(**name):   #takes as a dictionary 
    print("hello," , name["fname"],name["mname"],name["lname"])


name(mname="Shrikant",lname="Patil",fname="Aditya")


OUtput:

hello, Aditya Shrikant Patil.
==========================================================================================================================

# return Statement:

The return statement is used to return the value of the expression back to the calling function.

Example:

def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    
    return sum/len(numbers)


c=average(1,2,3,4,5)

print (c)

Output:

3
===================================================================================================================================
'''


def average(*numbers):  #takes as a tuple

    sum=0

    for i in numbers:
        sum+=i
    
    print("Averge : ",sum/len(numbers))


def name(**name):   #takes as a dictionary 
    print("hello," , name["fname"],name["mname"],name["lname"])


name(mname="Shrikant",lname="Patil",fname="Aditya")




