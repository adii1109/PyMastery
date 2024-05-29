"""
> Python Decorators:

python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and
methods. They are a way to extend the the functionality of function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behaviour of the 
orignal function the function is often referred to as a "decorated" function . The basic syntax for using a decorator is the following:


> Example : 

def greet(fx):
    def mfx():
        print("Good Morning ")
        fx()
        print("Thanks for using my funtion")
    return mfx

@greet    
def hello():
    print("Hello World")

hello()

-------------------------------------------------------------------------------------------------------------------------------------------------

> output:

Good Morning 
Hello World
Thanks for using my funtion

------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
# Args - args takes argumetns as a tuple
# kwargs - kwargs take argumets as a dictionary





def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning ")
        fx(*args,**kwargs)
        print("Thanks for using my funtion")
    return mfx

@greet    
def hello():
    print("Hello World")

hello()



@greet
def add(a,b):
    print(a+b)

add(1,2)


# greet(add) (1,2)
