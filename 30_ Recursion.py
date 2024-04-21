""""

Recursion in Python:

Recursion is the process of defining something in terms of itself

Example:

factorial (7)=7*6*5*4*3*2*1




"""

# 1] factorial using Recursion 

"""
factorial (7)=7*6*5*4*3*2*1
factorial (6)=6*5*4*3*2*1
factorial (5)=5*4*3*2*1
factorial (4)=4*3*2*1
factorial (3)=3*2*1
factorial (2)=2*1
factorial (1)=1
factorial (0)=1

we can write this above 
fact(n)=n*fact(n-1)

"""
def fact1(n):
    if (n==1 or n==0):
        return 1
    else:
       return  n*fact1(n-1)

factorial=fact1(5)
# print(factorial)


# 2 Fibbonachi Series

"""
0, 1, 1,2,3,5,8,13,21,34,55,89

a=0
b=1
c= (c-1)+(c-2)
"""

def fib(n):

    if (n==0 ):
        return 0
    elif (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

fib1=fib(5)

print(fib1)