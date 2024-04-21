"""
String Formating Using Format Method : 

String formating can be done in  python using the format method:
letter= "He my name is  {0} and I am from {1} "

country="India"
name="Adiya"

print(letter.format(name,country))

=====================================================================
String Formating Using F string  Method :

name="Adiya"
country="india"

letter=f"My name is {name} and i am from {country}"

print(letter)


============================================================================

iii]



"""

name=input("enter your name : ")
village=input('Enter your village name : ')

info=f'hello my name is  {name} form {village}'
print(info) # hello my name is  Aditya form Akurde


info1=f'hello my name is  {{name}} form {{village}}'
print(info1)  # hello my name is  {name} form {village}
