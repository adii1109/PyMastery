"""

Rasing Custom Erros :

> Sometimes We may need to create our own customs exceptions that serve our purpose.
> In python, we can define custom  

a=int(input('Enter the number between 5 and 9 : '))

if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9 ")

# OUtPUt==>

# Traceback (most recent call last):
#   File "e:\Python\38_Custom_Error.py", line 13, in <module>
#     raise ValueError("Value should be between 5 and 9 ")
# ValueError: Value should be between 5 and 9

"""

