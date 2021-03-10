#Simple game based off the card game war. 
#The individual with the highest card wins.
#That simple, enjoy

import random
import os

def deal():
  deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
  hand = []
  for i in range(1):
    random.shuffle(deck)
    card = deck.pop()
    hand.append(card)
  return hand

  
def check(computer, player):
  if computer > player: return 1
  else: return 2
  

def clear():
  if os.name == 'nt': os.system('CLS')
  if os.name == 'posix': os.system('clear')


def game():
  #Display result of the game
  computer = deal()
  player = deal()
  print("The computers card is ", computer)
  print("Your card is ", player, " \n")

  #Check for winner
  winner = check(computer,player)
  if winner == 1: print("You lose!")
  elif winner == 2: print("You win!")
  else: 
    print("There was a tie")
    game()

  #Check to continue game
  exit_game = input("Do you want to exit game enter y ").lower()

  if exit_game == "y":
    print("Thanks for playing \n")
    clear()
  else:
    player = []
    computer = []
    clear()
    game()


if __name__ == "__main__":
  print("WELCOME TO WAR \n")
  game()
