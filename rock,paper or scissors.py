import random


def play_game():
    user = input("please type any of the following words (pa for paper, ro for rock, and sci for scissors).\n").lower()
    computer = random.choice(["pa","sci","ro"])

    if user == computer:
         return "tie!"
    
    
    if user_won():
        return "You Win"

    return "You Lose"


def user_won(player,opponent):

    if ((player == "pa" and opponent == "ro" )
      or (player == "ro" and opponent == "sci" )
      or (player == "sci" and opponent == "pa" )):
      return True
      
    else:  return False


print(play_game())

    



    
