import random

def play():
    user=input("please type any of the following words (pa for paper, ro for rock, and sci for scissors).\n").lower()
    computer=random.choice(["pa","sci","ro"])

    if user==computer:
         return "tie!"
    
    
    
    



    
