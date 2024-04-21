''''
Python Lists

> Lists are ordered collection of data items.
> They store multiple items in a single variable.
> List items are separated by commas and enclosed within square
> Lists are changeable meaninig we can after them after creation.


Example:

marks=[98,99,100,97,95,"pass",True]

print(marks)
print(marks[0])
print(marks[1])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[6])


Output:

[98, 99, 100, 97, 95, 'pass', True]
98
99
97
95
pass
True

As we can see, a single list can contain items of different data types.

=========================================================================================

List Index

Each item/element in a list has its own unique index . This index can be used to access any particular
item from the list. The first item has index [0] ,second item index [1], third item has index[2] and so on.

Example:

colors = ["Red","Green","blue","Yellow","GREEn"]
            [0]  [1]      [2]      [3]     [4]


=========================================================================================
# Accessing list items

We can access list items by using its index with the square bracket syntax[], for example colors(0) will
give "Red",colors[1] will give "Green " and so on..


Positive Indexing:

As we have seen that items have index, as such we can access items using these indexes

=============================================================================================
#List Comprenhesion

list=[Expression(item) for item in itreable if condition]

Expresion = It is the item which being itrable
itrable = it can be list , tuple dictionary,sets and even in arrays and strings.
Condition= Condition check if the item should be added or not

lst0=[i for i in range(4)]
print(lst0)

OUtput: [0, 1, 2, 3]

lst=[i*i for i in range(10) if i%2==0]
print(lst)

Output : [0, 4, 16, 36, 64]

'''

import math as m

lst=[ m.pow(i,3) for i in range(5)  if i%3==0]

print(lst)