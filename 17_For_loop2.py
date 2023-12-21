

#practice Question


# Q.1 Sum of 1 to n number

# num=int(input('Enter the Number : '))

# sum=0

# for a in range(1,num+1):
#     sum+=a

# print(sum)


# =========================================================================

#Q2. Prime or not 

# num=int (input('Enter the number: \n'))

# isprime=True

# if (num<2):
#     isprime=False



# for a in range(2,num):

#     if (num%a==0):
#         isprime=False



# if(isprime==True):
#     print("prime")

# else:
#     print("Not prime")




# =========================================================================


#pattern Question

    # // 1
    # // 23
    # // 456
    # // 78910


# num=int(input('Enter the number : '))
# count=1
# for row in range (1,num+1):

#     for col in range(1,row+1):

#         print(count , end=" ")
#         count+=1
    
#     print()

# =========================================================================


    # // *
    # // **
    # // ***
    # // ****



# num=int(input('enter the number : '))


# for row in range(1,num+1):

#     for col in range(1,row+1):

#         print("*",end=" ")

#     print()


#============================================================================================================


# Sum of Even number between 2 to 100;


sum=0

for a in range(2,101,2):

    sum+=a


print(sum)
