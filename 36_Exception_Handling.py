"""
Exception Handling: 

Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
Exception Handling deals with these events to avoid the program runs. Exception handling deals with these evets to
avoid the program or system crashing and without this process, exception would discrupt the normal operation of a program.

Exception in Python :

Python has many build-in excptions that are raised when your program encounters and error 
when these exception occur, the python interpreter stops the current process and
passes it to the calling process until it is handled. if not handled ,the program will
crsh

> Python try...except:
try... except blocks are used in python to handel errors and exception The code in try  block runs when
there is no error. if the try block catches the error, then the except block is excuted.


"""

a=(input("Enter the number : "))

try : 
    for i in  range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except Exception as e:
    print("some Errors occureed: ", e)

print("Some lines of Codes")
print("end the programer")