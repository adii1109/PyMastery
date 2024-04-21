"""
Short hand if-else

There is also a shorthand syntax for the if-else statement that can be used when the conditioon
being tested is simple and the code blocks to be executed are short. 

Syntax: 

a=2
b=330

print("a") if a>b else print("b")


"""

age=int(input('Enter your age: '))

print("you can drive") if age > 18 else print("We can think about you ") if  age==18  else print("you cant drive")