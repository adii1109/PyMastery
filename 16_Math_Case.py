
x=int(input('Enter the age : '))

match x:

    case 18:
      print("Wek can think About You ")

    case _ if  (x>18 and x<=75):
        print("you can drive")

    case _ if (x<18 and x>75):
        print("you can't drive")

    case _ if (x>75):
        print("You cant drive")
    





"""

#Math Case :

    Math case like swich Case like cpp or java

    break keyword is not allowed



"""