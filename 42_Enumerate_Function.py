""""
Enumerate function in Python

The enumerate function is build-in-function in python that allows you to loop over a sequence
(such as a list , tuple, or string) and get the index and value of each element in the sequece at the same
time , 


syntax: 

for a, marks in enumerate(marks):
    if (a==0):
        print(marks)
print('Thank You ')


> Changing the Start Index:

by default, the enumerate fuction start the index at 0, but you can specify a different 
starting index by passing it as an argument to the enumrate function .



marks=[92,90,22,44,29,95,89]

# a=1
# for i in marks:
#     if (a==5):
#         print(i)
#         break
#     else:  
#         a+=1

for a, marks in enumerate(marks, start=1):
    if (a==1):
        print(marks) # Ouput == 92
print('Thank You ')

"""

marks=[92,90,22,44,29,95,89]

# a=1
# for i in marks:
#     if (a==5):
#         print(i)
#         break
#     else:  
#         a+=1

for a, marks in enumerate(marks, start=1):
    if (a==1):
        print(marks) # Ouput == 92
print('Thank You ')