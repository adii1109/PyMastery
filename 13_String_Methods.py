'''
-------------------Strings are immutable------------------------


String methods 

Python provides a set of build-in-methods that we can use to alter and modify the strings.

-------------------------------------------------------------------------------------------------

#Upper():
The upper()method converts a string to upper case..


Example:
Str1="AbcDEfghIJ"
print(str1.upper());

OUtput:
ABCDEFGHIJ

-------------------------------------------------------------------------------------------------
#lower():
The upper()method converts a string to lower case..


Example:
Str1="AbcDEfghIJ"
print(str1.lower());


Output:

abcdefghij

-------------------------------------------------------------------------------------------------

#strip():

The strip() method remove any white spaces before and after the strings.

Example:

str2= "   Aditya Patil     "
print(str2)


output:

Aditya Patil
---------------------------------------------------------------------------------------------------
#rstrip():

the rstrip() removes any trailing characters. Example


str3="hello !!!"

print(str3.rstrip("!"))

Output:

hello

-------------------------------------------------------------------------------------------------
#replace():

The replace () method replace all occurence of a string with another string . example

str2="Ashwin patil"

print(str2.replace("Ashwin","Aditya"));

Output:

Aditya Patil

-------------------------------------------------------------------------------------------------

#split():
The split method splits the given string at the specified instance and returns the sparated 
strings as list items

str2="Aditya patil"
print(str2.split(" ")) //Splits the strings at the whitspace " ".

OUtput:
['Aditya','Patil']
There are various other string methods that we can use modify our strings

-------------------------------------------------------------------------------------------------

Capitalize(): 

The capitalize() method turns only the first character of the string to  uppercase and the rest other
characters of the strings are turned to lowercase . The string has no effect if the first character is 
already uppercase

str1="hello'
str2="aditya"

print(str1.capitalize())
print(str2.capitalize())
-------------------------------------------------------------------------------------------------
#Center():

The center()method aligns the string to the center as per the parameters given by the
user

Example:
str1="Welcome to the Console !!!"

Output:

            Welcome to the Console !!!
            

We can also providde padding character.it will fill the rest of the fill character provided by the user.

Example:

str1= "Welcome to the Console!!!"
print(str.center(50,"."))


Output:

   ..................Welcome to the Console !!!................

-------------------------------------------------------------------------------------------

#Count():

The count() method returns the number of times the given value has occured within the given 
string


Example:

str2="Abracadabra"
coutStr=str2.count("a")
print(countStr)


Output:

4


-------------------------------------------------------------------------------------------


'''


