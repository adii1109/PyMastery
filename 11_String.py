'''
What are Strings?

In python, anything that you enclose between single or double quotation marks is considered a string . A
string is essentially a sequence or array of textual data Strings are used when working with Unicode
characters.
-------------------------------------------------------------------------------------------------
#Examples

name : Adiii
print("hello", adii)  // Hello Adiii

NOte: it does not matter whether you enclose your strings in single or double qutes ,the output
remains the same

Sometimes,the user might need to put quotation marks in between the strings. Example,consider
the : he said, "I want to eat an apple".

apple='he said , "I want to eat an apple".'

print(apple)

-------------------------------------------------------------------------------------------------

#   Multiline Strings


if our strings has multiple lines , we can create them like this:

mi="""
Mi squad
1.Rohit sharma
2.ishan kishan
3.surya
4.tilak
5.pandya
6.nehal
7.tim david
8.piyush chawala
9.jasprit bumrah
10.akash madwal
11.Jason Benhrodroff
"""
print(mi)

-------------------------------------------------------------------------------------------------

#Accessing Characters of a string

In python, strings is like an array of characters. we can accesss parts of strings by using its index which
starts from 0.
Square brackes can be used to access elements of the string

name=Aditya


print(name[0]) // A
print(name[1]) //d

#Looping through the string

We can loop through string using a loop like this:

for character in name:
    print(character);

output:
A
d
i
t
y
a

-------------------------------------------------------------------------------------------------
'''

mi='''
Mi squad
1.Rohit sharma
2.ishan kishan
3.surya
4.tilak
5.pandya
6.nehal
7.tim david
8.piyush chawala
9.jasprit bumrah
10.akash madwal
11.Jason Benhrodroff
'''


print(mi)