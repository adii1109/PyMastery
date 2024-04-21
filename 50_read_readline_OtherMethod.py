"""
> Readlines() Method :

The readline () method reads a single line from the file. if we want to read multiple lines, we can use loop


# Readline Method (): 

a=open("myfile.txt","r")

while(True):
    line=a.readline()
    if not line:
        break
    print(line)

> NOte: 
The readlines() method reads all the lines of the file and returns 
them as a list of strings.

Program : 
# 72,88,79
# 45,40,49
# 53,70,65



# f=open("myfile_marks.txt","r")

# i=0
# while(True):
#     i+=1
#     line=f.readline()
#     if not line or i==2:
#         break
#     m1=line.split(",")[0] #72 
#     # print(m1)
#     m2=line.split(",")[1] #88
#     # print(m2)
#     m3=line.split(",")[2] #79
#     # print(m3)
    

#     print(f"Marks of student {i} in Maths is : {m1}")
#     print(f"Marks of student {i} in English is : {m2}")
#     print(f"Marks of student {i} in Computer is : {m3}")

==========================================================================================
> Writelines () Method():

The writelines() method in python writes a sequence of strings to a file . the sequence can
iterable object , such as a list or a tuple

Code:
f=open("myfile3.txt","w")

i=1
while (i<=100):
    lines= [f'line no {i} \n']
    f.writelines(lines)
    i+=1

f.close()


Writelines method:
> this will write the strings in the lines list to the file myfile3.txt . 
> The \n characters are used to add newlines characters to the end of each string
> keep in mind that the writelines () method doe not add newlines characters between the strings in the sequence.



"""

# Readline Method (): 

# a=open("myfile.txt","r")

# while(True):
#     line=a.readline()
#     if not line:
#         break
#     print(line)


f=open("myfile3.txt","w")

i=1
while (i<=100):
    lines= [f'line no {i} \n']
    f.writelines(lines)
    i+=1

f.close()

   