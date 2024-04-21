"""
how importing in python works

Importing in python is the process of loading code from a python module into current script.
This allows you to use the function  and variable defined in the module in your  current script, as 
well as any additional modules that the imported module may depend on..

to import a  module in python , you use the import statement follwed by the name of module.
for example, to import the math module , which contains a variety of mathematical function , you would 
write

example

import math

result =math. sqrt(9)
print (result) # output=3.0
-------------------------------------------------------------------------------------------------------------------

> From Keyword 
You can also specific function or variable from a module using the from keyword. for
example, to import only the sqrt function from the math module , you would write:


from math import sqrt

result=sqrt(9)
print(result)

You can also import multiple functio or variable at once by separating them with a comma:
from math import sqrt,pi

result=sqrt(9)
print(result) # 3.0

print(pi) # 3.141592653589793

-------------------------------------------------------------------------------------------
> importing everything

it's also possible to import all function and variable from a module using * wildcard.
however, this generally not recommended as it can lead to confusion and make it harder to 
understand where specific function and variable coming from.

from math import *

result=sqrt(9)
print(result) # 3.0

print(pi) # 3.141592653589793

--------------------------------------------------------------------------------------------------
> The "As" Keyword 

import math as m

result=m.sqrt(9)
print(result) # 3.0

print(m.pi) # 3.141592653589793
--------------------------------------------------------------------------------------------
> The dir function

finally, python has build-in-function called dir that you can use to view the names of all the 
function and variable defined in a module . this can be helpful for exploring and understanding the contents
of a new module.

import math as m

print(dir(m))

output==> 

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 
'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 
'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi',
 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

"""



from Gra import thankYou,Universe

Universe()
print(thankYou)

# Output:
# thank you unvierse, thank you so much god, thank you :),Jay shri Ganesha, Jay Shri ram
# thank You Unvierse :)