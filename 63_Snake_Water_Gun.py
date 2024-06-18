"""
 > Snake , Water , Gun Rules:


 if Comp= snake , You = Water ,  Win= snake
 if Comp= snake , You = Gun ,    Win= gun
 if Comp= Gun ,   You = Water ,  Win= water
 if Comp= Gun ,   You = Snake ,  Win= gun
 if Comp= Water , You = Snake ,  Win= snake
 if Comp= Water , You = Gun ,    Win= Water
 


"""

import random as r

game=['s','g','w']

name=input("Enter Your name : ")


def Game():
    ans=0
    Comp=r.randint(0,2)
    
    print("""please Select , 
        0 For Snake
        1 For Gun
        2 For Water
        """)

    you=int(input("Enter here: "))
    print(f"{name} Select : {game[you]}")
    print(f"Computer Select : {game[Comp]}")



    if ( game[Comp]=='s' and game[you]=='w'):
        ans="Computer Win"

    elif ( game[Comp]=='s' and game[you]=='g'):
        ans=f"{name} Win"

    elif ( game[Comp]=='g' and game[you]=='w'):
        ans=f"{name} Win"

    elif ( game[Comp]=='g' and game[you]=='s'):
        ans="Computer Win"

    elif ( game[Comp]=='w' and game[you]=='s'):
        ans=f"{name} Win"

    elif ( game[Comp]=='w' and game[you]=='g'):
        ans="Computer Win"

    else:
        ans="Draw"


    return ans

print(Game())