

# Calculator using Function

def calculator(a,b,op):

    if (op=="+"):

        print(a+b)

    elif (op=="-"):

        print(a-b)

    elif (op=="*"):

        print(a*b)

    elif (op=="/"):

        print(a/b)

    else:
        print("Choose right operator ,try again ")

Num1=int(input('Enter first number : '))
Num2=int (input('Enter second number : '))
operator=input('Enter the operator : ')

calculator(Num1,Num2,operator)


"""
Python Function

A function is a block of code that performs a specific task whenever it is called. In bigger programs, amount of code,
it is adivisable to create or use existing function that make the program flow organized and neat.


There are two types of function:

> Build-in function 
> User-defind Function


# Bulit -in functions:

These function are defined and pre-coded in python. Some examples of build fuctions are 
as follows:

min(),max(),len(),type(),range(),dict(),list(),set(),tuple(),set(),print(),etc


# User-defined Function:

We can create function to perfrom specific tasks as per our needs. Such function are called user-defined function.

================================================================================================================================

Syntax:

def function_name(parameter):
        pass
        #code and Statement


        
> Create a function using the def keyword, followed by a function name, followed by a
    paranthesis(()), and a colon(:)

> Any parameters and arguments should be placed within the parentheses.

> Rules to naming functon are simlar to that of naming variables.
> Any Statements and other code within the function should be indented.


# Calling a function:

We call a function by giving the function name, followed by parameter (if any) in the parenthesis


Example:
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)


# x=7
# y=5

# calculateGmean(x,y)


Output:

 2.9166666666666665

"""


def calculateGmean(a,b):

    mean=(a*b)/(a+b)
    print(mean)


# x=7
# y=5

# calculateGmean(x,y)
    

def isGreater(a,b):

    if (a==b):
        print("both numbers are same ")
    
    elif (a>b):
        print("first number is Greater ")

    elif (a<b):
        print("Second number is Greater ")

    else:
        print("Error..")


# c=int(input('enter the number '))
# d=int (input('Enter the number '))

# isGreater(c,d)
        

def binod():
    print('Mai Ghar mai khana khaunga , tumh cantain mai khao bhaii')


def islesser():
    pass    #badmai aake dekhunga , aabhi kuch mat karo 