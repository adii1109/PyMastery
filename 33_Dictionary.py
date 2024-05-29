"""
Dictionary : 

> Dictionary are ordered collection of data items
> They store multiple items in a single variable
> Dictionary items are key-value pair 
> key-value pair separted by commas and enclosed within curly brackets {}

Example:
> info={'name':'aditya','age':19, 'class': 15}

I}Accessing single values:
> values in a dictionary can accessed using keys.
> we can accessed dictionary values by mentioning key either in square brackets or by using get method.

> example: 

info={'name':'aditya','age':19, 'class': 15}

print(info['name']) # aditya

# in this method if this key is not present then show error

print(info.get('name'))  # aditya
print(info.get('gender')) #none
# in this method if this key is not present then not showing error
=============================================================================================================================================

II} Accessing multiple values:
> we can print all the values in the dictionary using values() method .

example:

print(info.values()) # dict_values(['aditya', 19, 15])

==============================================================================================================================================
III}accessing keys():
> we can print all the keys using the keys() method
print(info.keys())  # dict_keys(['name', 'age', 'class'])

===============================================================================================================================================


for key in info.keys():
    print(f"the value of correspounding to the {key} is {info[key]}")

# the value of correspounding to the name is aditya
# the value of correspounding to the age is 19
# the value of correspounding to the class is 15
=============================================================================================================================================
IV} Accessing key-value pairs:
we can print all the key-value pairs in the dictionary using items() method.


print(info.items())
# dict_items([('name', 'aditya'), ('age', 19), ('class', 15)])


"""

info={'name':'aditya','age':19, 'class': 15}

print(info['name']) # aditya

# in this method if this key is not present then show error

print(info.get('name'))  # aditya
print(info.get('gender')) #none
# in this method if this key is not present then not showing error


print(info.values()) # dict_values(['aditya', 19, 15])
print(info.keys())  # dict_keys(['name', 'age', 'class'])

# for key in info.keys():
#     print(f"the value of correspounding to the {key} is {info[key]}")

# the value of correspounding to the name is aditya
# the value of correspounding to the age is 19
# the value of correspounding to the class is 15


print(info.items())
# dict_items([('name', 'aditya'), ('age', 19), ('class', 15)])

for key,value in info.items():
    print(f"the value correspounding to the {key} is {value}")