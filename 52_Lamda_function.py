"""
> Lambda function in Python 

In python, a lambda function is a small anonymous function without a name. it is defined using the 
lambda keyword and has the following syntax:

syntax:
lambda arguments : expression 

Code: 


# Function to double the input

def double(x):
    return x*2

#Lambda function to double the input

double=lambda x: x*2


print(double(5)) #ans ==> 10

""" 

cube= lambda x:x*x*x

def appl(fx,value): # funtion as a agrument
   return 6+fx(value)

# print(appl(cube,2)) 
br=0
while(True):
    if (br==1):
        break
    else:

        x=int(input('Enter the first num: \n'))
        y=int(input('Enter the Second num: \n'))
        op=input('Select the operator : "+,-,*,/"  ')


        if op=='+':
            add= lambda x,y: x+y
            print(add(x,y))
        elif op=='-':
            sub= lambda x,y: x-y
            print(sub(x,y))
        elif op=='*':
            multi= lambda x,y: x*y
            print(multi(x,y))
        elif op=='/':
            div= lambda x,y: x/y
            print(div(x,y))
        else:
            print("error : ")

        print('thank  you Unvierse  :) ')

    yn=input("stop the calci select : 'y/n' ")

    if(yn=='y'):
        br=1

    

