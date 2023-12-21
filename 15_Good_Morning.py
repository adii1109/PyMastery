import time

timestamp=time.strftime('%H:%M:%S')


hour=int(time.strftime('%H'))
minite=int(time.strftime('%M'))
second=int(time.strftime('%H'))


if (hour>=12 and hour<=16):
    print("Good Afternoon Sir")

elif (hour>16 and hour<=20):
    print("Good Evening sir")

else:
    print('Good Morning sir , Have a Good Day ! ')

print("Thank You Universe :)")