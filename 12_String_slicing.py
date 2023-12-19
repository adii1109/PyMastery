
'''
String Slicing & Operations on String


#Length of a string

We can find the lenth of a string using len() function

Example:
fruit="Mango"
len1=len(fruit)
print("mango is a ", len1, "letter  word.")

Output:
Mango is a 5 letter word.


#String as an Array 

A string is essentially a sequece of characters also an array. Thus we can access the elements of this 
array

Example:

pie="Apple"
print(pie[:5]) 
print (pie[6]) # returns character at specified index error



'''

fruit="Apple"

appleLen=len(fruit)

print("apple lenth =>", appleLen)

print(" fruit[0:] =>" , fruit[0:]) #apple

print(" fruit[:5] =>" , fruit[:5]) #apple

print(" fruit[0:-3] =>" , fruit[0:-3]) #ap

print(" fruit[-1:len(fruit)-3] =>" , fruit[-1:len(fruit)-3]) #not make sence 

# if negative in case : [len(fruit) - negative value] 
# it makes sence otherwise , return blank space



# Quiz Quiz

name="harry"

print(name[-4:-2]) #ar