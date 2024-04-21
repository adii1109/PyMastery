"""
>> if "__name__==__main__ " in python

The if __name__==__main__  idion is common pattern used in python scripts to determine wehter the script 
is being run directly or being imported as a module into another script

in Python, the __ name__ variable is a build-in-variable that is automaticaly set to the the name of current module. 
when a python script is run directioly , the --name-- varialbe is to the __main__ wehen the script is importand as a module
into another script, the __name__ variable is set to the name of the module


>> Why is it useful?
This idiom is useful because it allows you to refuse code from a script by importing it as a module
into another script , without running the code in the original script 
for example


"""

import Gra 


#befor using if name== "main":
Gra.Universe()

# OUtput : 
# thank you unvierse, thank you so much god, thank you :),Jay shri Ganesha, Jay Shri ram
# thank you unvierse, thank you so much god, thank you :),Jay shri Ganesha, Jay Shri ram


# =============================================================================================

# After using if name== "main":

Gra.Universe()

# OUtput:
# thank you unvierse, thank you so much god, thank you :),Jay shri Ganesha, Jay Shri ram