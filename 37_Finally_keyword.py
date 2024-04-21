"""
Finally Clause :

> The finally code block is also part of exception handling. When we handle exception using the try and except block , we can 
include a finally block at the end . 

> The finally block is always executed, so it is generally used for doing the concluding tasks like
closing file resources or closing database connection or may be ending the program exceution 
with delightful messages.



"""

def fun1():
    try:
        l=[1,5,6,7]
        i=int(input('Enter the index: '))
        print(l[i])
        return 1
    except:
        print("Some error occured ")

    
    finally:
        print("I'm Alawys Executed")

    print("I'm Alawys Executed") # THIS IS NOT WORKING IN FUNCTION 

    # ABVOE STATEMENT WORK NORMAL CODE BUT WHEN YOU WANT ALWAYS CODE IN FUNCTION USE FINALLY KEYWORD
    

x=fun1()
print(x)