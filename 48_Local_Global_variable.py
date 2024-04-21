"""
> Local and Global Variable:


> A local variable is a variable that is defined within a function and only accessible within that 
funcition and is only accessible within that function . it is creted when the fuction is called and is 
destroyed when the function return 

> a global variable is variable that is defined outside of a function and is accessible from within any 
function in your code


Example: 
-------------------------------------------------------------------------------------------------------------

x=10 # global variable 


def myfuction():
    y=5  # local variable 
    print(y)



myfuction() #5 
print(x) #10
# print(y) # this will cause an error because y is local variable and it is not acciable outside of function 

================================================================================================================
> Global Keyword :


The global keyword is used to declare that a varialbe global variabl and should be accessed from the global scope. here's an 


Imp : When you use global keyword in function after you you want change variable value using global and if you dont call function 
global keyword is not working 

example:



"""
x=10 # global variable 


def myfuction():

    global x
    x=23
    y=5  # local variable 
    print(y)



myfuction() #5  [ if you  dont call myfunction , global keyword not work ]
print(x) #10 {23 , when global use}