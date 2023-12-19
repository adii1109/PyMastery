'''
In python , we can take user input directly by using input() fuction . This input fuction
gives a return value as string / character hence we have to pass that into a variable
-------------------------------------------------------------------------------------------------

#Syntax:
variable=input()

but input function returns the value as string . hence we have to typecast them whenver 
required to another datatype.

-------------------------------------------------------------------------------------------------
#Example:

variable=int(input())
variable=float(input())


we can display a text input function. This wil make input() function take user input 
display a message well


##Input takes default string
'''




a=input("Enter your Name : ")



print("My name is ", a)


first=input("Enter your first number : ")
second=input ("Enter your second number : ")


print(first+second)

print(int(first)+int(second))