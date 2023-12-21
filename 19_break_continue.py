'''

break Statement 

The break statement enbles a program to skip over a part of the code. A break statement terminates the 
very loop it lies within .


for i in range (1,50,1):
    print(i,end=" ")

    if (i==50):
        break
    else:
        print('Mi')

print("Thank You Universe ")

==============================================================
#Continue Statement 

The continue statement skips the rest of the loop statemets and causes the iteration to occur

Example:
for i in [2,1,25,32,535,234,21,50]:

    if (i%2!=0):
        continue

    print(i)

Output:
2
32
234
50

 

'''

for i in [2,1,25,32,535,234,21,50]:

    if (i%2!=0):
        continue

    print(i)
# ======================================================================================================

# Do -while loop in python

#Do while looops one's time always.
    
    

i=0

while True:
    print(i)
    if(i==10):
        break
    i+=1