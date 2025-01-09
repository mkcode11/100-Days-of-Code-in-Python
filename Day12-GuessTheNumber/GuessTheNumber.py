import random
import art
import os

def choiceNumber():
  num=random.randint(0,100)
  return num


def play(attempts):
  is_game_over=False 
  num=choiceNumber()
  print(f'I\'m thinking of a number between 1 to 100.')
  while not is_game_over:
    print(f'\nYou Have {attempts} remaining to guess the number.')
    guess=int(input(f'Make a guess : '))
    if guess==num and attempts>=0:
      print(art.won)
      is_game_over=True
    elif guess<num:
      print('Too Low')
    elif guess>num:
      print('Too High')
    attempts-=1
    if attempts==0:
      print(art.lose)
      if input('Do You Want to play Again? Type \'y\' or \'n\' : ')=='y':
        os.system('cls')
        choice()
      else:
       print(art.bye)
       is_game_over=True

def choice():
  print(art.logo) 
  if input('  Welcome to the Guess The Number.\n  Choose Difficulty : Type \'easy\'(10 attempts) or \'hard\'(5 attempts) : ')=='hard':
    play(5)
  else:
    play(10)

choice()