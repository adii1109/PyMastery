"""

# Manipulating Tuples :

Tuples are immutable , hence if you want to add, remove or change tuple items

> first you must convert the tuple to list
> perform operation on list
> Convert List to tuple 

"""


countries=('Spain','Italy','India','England','Germany')

# print(type(countries))
print("Before Operation on Tuple : \n",countries)

# "Output ==>
#  <class 'tuple'>
# ('Spain', 'Italy', 'India', 'England', 'Germany')"

temp=list(countries)

temp.append("Turkey")
temp.append('Bhutan')
temp.append('New zaland')

temp.pop(1)

countries=tuple(temp)
print("After  Operation on Tuple : \n",countries)

print("Thank You Universe :)")
