"""
> Is vs "==" :

 In these cases, a and b both pointing to the same object in memory, so is and == both return true

 For mutalbe object such as list and dictionaries , 'is' and '==' can behave differently
 in genral , you should use "==" when you want compare the values of two objects , and use is when 
 you want check if two objects are the same object in memory.



"""

a=4
b="4"


print(a is b) # False 
print(a == b) # false

c=[1,2,43]
d=[1,2,43]


print(c is d) # Exact location of object in memory  {identity}
# ==> False
print(c==d) # value Check 
# ==> True


# Note : immutable values if same then both values , e is f and e==f is true 


e=(1,2)
f=(1,2)

print(e is f) # true 
print(e==f) # true 


g="harry"
h="harry"


print(g is h) # true
print(g==h)   #true

# both are true because of string are immutable

x=3
y=3


print(x is  y ) # true
print(x==y)     #true

# both are true because immutable
