"""

Doctstring in Python:

Python doctstring are the string literls that apper right after the defination of function , mehthod , class or Module 



"""


def square(n):
    ''' Takes in a number n , return the square of n '''
    print(n*n)


#this syntax of getting information function , method or class :
print(square.__doc__) #Takes in a number n , return the square of n


square(5)