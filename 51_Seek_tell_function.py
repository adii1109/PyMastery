"""
SeeK() and tell() function :

In python , the seek () and tell() function are used to work with file objects and their position within a file.
these function are part of the build-in io module , which provdes a consistent interface for reading and writing to various 
file-like objects, such as files, pipes and in-memory buffers.

> Seek() funtion :

The seek() function allows you to move the current position within a file to a specific point 
the position is specified in bytes,and you can move either forward or backward form the current position for.
example.


Code: 

#file5.txt =123456789tettff

with open ("file5.txt","r") as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    data=f.read(5)
    print(data) # ettff
--------------------------------------------------------------------------------------------------------------------------------
tell():
The tell() function returns the current position within the file, in bytes . This can be useful for keeping track of your 
location within the file or for seeking to a seeking to a specific position relative to the current position. for example:

Code:
with open ("file5.txt","r") as f:
    # Move to the 10th byte in the file
    f.seek(10)

    current_position=f.tell()

    print(current_position) #==> 10
    # tell function tell seeking position

    # read the next 5 bytes
    data=f.read(5)
    print(data) # ettff
==============================================================================================
truncate() function

When you open a file in python using the open function , you can specify the mode in which you want to open the file
If you specify the as "w" or "a", the file is opened in write mode and you can write to the file. However, if you want to 
truncate the file to a specific size, you can use the truncate function

"""

with open('sample.txt','w') as f:
    f.write('hello world!')
    f.truncate(5)

with open ('sample.txt','r') as f:
    print(f.read()) # hello 