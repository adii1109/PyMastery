
#  Simple Calculator Using If-else Statement 

num1=int(input("Enter Your first number : "))
num2=int(input("Enter Your second  number : "))
operator=input("Enter the Operator : ")


if (operator=='+'):
    print("Addittion is:", num1+num2)

elif (operator=='-'):
    if (num1>num2):
        print("Subtraction is : ", num1-num2)

    else:
        print("Subtraction is : ", num2-num1)

elif(operator=='*'):
    print("Multipication is : ", num1*num2)

elif(operator=='/'):
    print("Division is : ", num1/num2)

else:
    print("error")

print('Thank You Universe :)')

#----------------------------------------------------------------------------------------------------
# Number Check Positive , negative or zero 



# num=int(input("Enter the number : "))


# if (num>0):
#     print("Positive number.")

# elif(num==0):
#     print("zero")

# else:
#     print("Negative-num")



#--------------------------------------------------------------------------------------------------


'''
# if-else Statements

Sometimes the programmer need to check the evaluation of certain expression(s),whether 
the expression(s) evaluate to True or False. if the expression evaluates to False,the the 
program execution follows a different path than it would have if the expression had evaluated to true.

Based on this , the conditional statement are further classified into following types:

> if
> if-else
> if-else-elif
> nested if-else-elif.

'''