"""
> Map , Filter and Reduce

In Python , the map,filter and reduce function are build-in function that allow you to apply a function to a  sequence of element and return a 
new sequence . these function are known as higher-order function, as they take other 
function as agruments

> Map :

The map function applies a function to each element in a sequence and returns 
a new sequence containing the transformed elements. The map function has 
the following syntax:

map(function, iterable)

The function argument is a function that is applied to each element in the itrable argument. 
the iterable argument can be a list, tuple or any other iterable object.

Code:

def cube(x):
   return x*x*x

l=[1,2,4,8,10]


#Using regular Method : 

# newl=[]
# for i in l:
#    newl.append(cube(i))

# print(newl)


#Using map method : 

newl=list(map(cube,l))
print(newl)

# output =>  [1, 8, 64, 512, 1000]

In the above example, The map function applies the function to each element in the list and returns 
a new list containg 
=================================================================================================================
> Filter :

The filter function filters a sequence of element based on a given predicate.
function that return a boolean value  and return a new sequence containing only the 
elements that meet the predicate. The filter function has the followin 

syntax:

filter(predicate,iterable)

the predicate argument is a function that returns a boolean value and is applied to each element
in the iterable argument . the iterable argument can be a list , tuple or any other iterable 


Code :

l=[1,2,4,8,10,20,3,5,7,9,16,28]


def filter_function(x):
    if (x%2==0):
        return x  [true return 1 , false retun 0]

newl=list(filter(filter_function,l))

print(newl)
# output => [2, 4, 8, 10, 20, 16, 28]
======================================================================================================================================

Reduce:
The reduce function is a higher-order function that applies a function to a sequence and returns a 
single value . It is a part of the funtools module in python and has following 

syntax:

from functools import reduce

numbers=[1,2,3,45,9]

sum=reduce(lambda x,y : x+y,numbers)

print(sum)
Output => 60

in the above example , the reduce function applies the lambda function lambda x,y: x+y to the elements in numbers list. The lambda function 
adds the two arguments x and y and returns the result. The lambda fuction adds the two aragument x and y and returns the result . The reduce function 
applies the lambda function to the fist two elements in list ( 1 and 2 ) then applies the 
function to the result(3) and the next element(3) and so on. The final result is the sum of all the elements in the list ,
which in 60.

it is important to note that the reduce function requires the funtools module to be imported in order to use it.

"""
