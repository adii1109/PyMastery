"""
__ File Handling in Python ___

> Opening a file

python provides the open () function to open a file.  It takes two agruments : the name of 
the file and the mode in which the file should be opened . The mode can be 'r' for reading, 'w' for writing
or 'a' for appending.

example open a file for reading:

f=open('myfile.txt','r')

by default , the open function returns a file object that can be used to read from or write to the file , depending on the mode


> MOdes in files

1. read(r): This mode open the for reading only and gives an error if the file does not exist . 
this default mode if no mode is passed as a parameter

2. write(w): This mode opens the file for writing only and creates a new file if the file does not exist.

3. append(a): This mode opens the file for appending only and creates a new file 
if the file does not exist.

4. create(x): This mode creates a file and gives an error if the file already exists.

5. text(t): Apart form these modes we also need to specify how the file must handled . t mode is used 
to handle text files . t refers to text mode. There is no difference between r and rt or w and wt since text
mode is the default . The default mode is 'r' (open for reading text, synonym of 'rt')
 
6. binary(b): used to handle binary files(images, pdfs, etc.)



---------------------------------------------------------------------------------------------------
Reading from a file:
Once we have a file object we can use various method to read from the file.

the read() method reads the entire contents of the file  an returns it as a string

Example: 
-----------------------------------------------------------------------------------------------------
f=open('myfile.txt','r')

print(f) 
# Output : <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>

text=f.read()

print(text)
f.close()

#OUtput : hey adii , your are so awesome man !
-----------------------------------------------------------------------------------------------------------
> Writing to a file
To write to a file , we first need to open it write mode 

Example write 

f=open('myfile2.txt','w')

f.write("hello adii") # clear the first data 

> Append method 


== keep in mind that writing to a file will overwrite its contents . if you want to append to a file insted of 
overwriting it you can open it in append mode

f=open('myfile2.txt','')

for i in range(1,101):
    f.write(f"\n Hello adii {i} ")


f.close()
-------------------------------------------------------------------------------- 
> Closing a file 
it is important to close a file after you are done with it. This releases the resource used  by the 
file and allows other programs to access it.

To close a file, you can use close() method

f=open ('myfile.txt','r')
# do something with the file
f.close
=========================================================================================
> The 'with' statement { Automatically close file}

Alternatively, you can use the with statement to automatically close the file after you are done with
it



"""
# Automatically close file
with open ('myfile.txt','a') as f:
    f.write('hey i am inside of with ')

# f=open('myfile2.txt','')

# for i in range(1,101):
#     f.write(f"\n Hello adii {i} ")


# f.close()