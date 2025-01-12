import random
import art
import os
from game_data import data


def randNum():
  num=random.randint(0,len(data)-1)
  return num

def selectperson(num):
  return f'{data[num]['name']} a {data[num]['description']} from {data[num]['country']}'

def compare(num1,num2):
  if num1>num2:
    return 'a'
  elif num2>num1:
    return 'b'


def play():
    is_game_over=False
    score=0
    print(f'{art.logo}')
    index_of_personA=randNum()
    while not is_game_over:
      # info of personA
      print(f'Compare A : {selectperson(index_of_personA)}')
      followerA=data[index_of_personA]['follower_count']
      print(followerA)

      print(art.vs)

      # info of personB
      index_of_personB=randNum()
      print(f'Against B : {selectperson(index_of_personB)}')
      followerB=data[index_of_personB]['follower_count']
      print(followerB)

      # guess and compare
      guess=input(f'Who has more followers? Type \'A\' or \'B\' : ').lower()
      if guess==compare(followerA,followerB):
        score+=1
        os.system('cls')
        print(f'{art.logo}\nYou\'re right! Current score: {score}.')
        index_of_personA=index_of_personB
      else: 
        os.system('cls')
        print(f'{art.logo}\nSorry, that\'s wrong. Final score: {score}\n')
        is_game_over=True
        choice()
        

def choice():
  if input('Do you want to play again : Type \'y\' or \'n\' : ')  =='y':
    os.system('cls')
    play()  
  else:
    os.system('cls')
    print('\nOk, Good Bye.\n')

play()
    

