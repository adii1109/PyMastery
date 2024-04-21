'''
Update():
The update() method update the value of the key provided to it the item already exists 
in the dictionary, elese it create a new key-value pair

info={'name': 'Karan','age': 19, 'eligible ': True}

print(info)

info.update({'age': 20})
info.update({'DOB': 2001})
print(info)

OUtput ==> {'name': 'Karan', 'age': 20, 'eligible ': True, 'DOB': 2001}


ii]
Empolyee preformance:
ep1={111:79,145:90,134:69,231:55}
ep2={646:89,653:77}

ep1.update(ep2)
print(ep1)

OUtput ==> {111: 79, 145: 90, 134: 69, 231: 55, 646: 89, 653: 77}

=====================================================================================================

Clear():

The clear() Method removes all the items form the list

info={'name': 'Karan','age': 19, 'eligible ': True}
info.clear()
print(info)

Output==> {}

============================================================================================================
Pop():
The pop() method removes the key-value pair whose keys is passed as a parameter


info={'name': 'Karan','age': 19, 'eligible ': True}

info.pop('age')
print(info)

OUtput ===> {'name': 'Karan', 'eligible ': True}
============================================================================================================
popitem():
The popitem() method removes the last key-value pair form the dictionary

info={'name': 'Karan','age': 19, 'eligible ': True}

info.popitem()
print(info)

OUtput ==> {'name': 'Karan', 'age': 19}

============================================================================================================
del():

We can also use the del keyword to remove a dictionary item
info={'name': 'Karan','age': 19, 'eligible ': True}

del info['age']
print(info)

OUtput ==> {'name': 'Karan', 'eligible ': True}




===============================================================================================================
ii]

we can delete entire dictionary using del keyword:

info={'name': 'Karan','age': 19, 'eligible ': True}
del info
print(info)

# Output ==> name 'info' is not defined
============================================================================================================


'''

