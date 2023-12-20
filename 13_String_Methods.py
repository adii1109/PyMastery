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
endswith():

The endswith() method checks if the strng ends with a given value . if yes then return true 
else return false.


Example:
str1="Welcome to the Console !!!"
print(str1.endswith("!!!"))


Output:

True

We can even also check for a value in-between the string by providing 
start and index position.


Example:
str1="Welcome to the Console !!!"
print(str1.endswith("to",4,10))


Output:

True

---------------------------------------------------------------------------------------------

find():

The find() method searches for the first occurence of the given value and returns the 
index where it is present . If given value is absent from the string the return -1;


Example:

str1="He's is Dan. He is an honest man."
print(str1.find("is"))


Output:

13

---------------------------------------------------------------------------------------------

index():

The index()method searches for the first occurence of the given value and returns the index
where it is present . if given vlaue is absent from the string then raise an exception.

Example:
str1="He's is Dan. He is an honest man."
print(str1.find("Danial"))


Output:

ValueError:Substring not found

---------------------------------------------------------------------------------------------
isalnum():

The isalnum() method returns True only if the entire string only consists of A-Z, a-z,0-9. If 
any other characters or punctions are present , then returns False.

Example:

str1="WelcomeTotheConsole"
print(str1.isalnum())

Output:
True


---------------------------------------------------------------------------------------------
isalpha():

The isalnum() method returns True only if entire string only consists of A-Z ,a-z, if
any other characters or punctions or number (0-9) are present, then it returns False.


Example:

str1="Welcome11"
print(str1.isalpha())

Output:

False

---------------------------------------------------------------------------------------------
islower():
The islower() method retuns True if all the characters in the string are lower case,
else returns False.


Example:

str1="hello world"
print(str1.islower())


Output:

True

---------------------------------------------------------------------------------------------

isprintable():
The isprintable() method returns True if all the values within the given string are printable
,if not then returns false.



Example:
str1="hello adii \n"

Output:
False

reason:
\n is not printalbe;

---------------------------------------------------------------------------------------------
isspace():

The isspace() method returns True Only if the string contians white spaces, else returns
False.

Example:
Str1="            " #using Spacebar
str2="            " #using tab
str3"Adii"


Output:

True
True
False


---------------------------------------------------------------------------------------------
istitle():

The istitle() returns True only if the first letter of each word of the string is capatalized
,else returns False.


Example:

str1="World Health Organization"
print(str1.istitle());


Output:
True


---------------------------------------------------------------------------------------------

title():

the title() method capitalizes each letter of the word within the string.

Example:

str1="He's name is adii. adii is an honest man. "
print(str1.title())


Output:

He's Name Is Adii. Adii Is An Honest Man.

---------------------------------------------------------------------------------------------


'''


