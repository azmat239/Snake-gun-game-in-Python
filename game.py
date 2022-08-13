from operator import truediv
import random

from flask import g

def game(comp,you):
    if(comp==you):
        return None
    elif comp=='s':
        if(you=='w'):
            return False
        elif you=='g':
            return True
    elif comp=='g':
        if(you=='s'):
            return False
        elif you=='w':
            return True        
    elif comp=='w':
        if(you == 'g'):
            return False
        elif you=='s':
            return True
    else:
        print("you have  entered the wrong character")
i='w'
while(i!='e'):
    you=input("user turn : Enter the character you want to choose snake-s gun-g water-w \n")

    print("Computer turn : \n")
    random_no =random.randint(1,4)
    if(random_no==1):
        comp='s'
    elif (random_no==2):
        comp='w'
    else:
        comp='g'
    print(f"comp={comp} you={you}")
    b=game(comp,you)
    if (b==True):
        print("You won the game  ")
    elif(b==None):
        print("It's a draw  ")
    else:
        print("You lost the game ")
    print("Enter e to exit otherwise press any key : ")
    i=input()


    