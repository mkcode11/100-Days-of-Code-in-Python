import random
import hangman_words
import hangman_arts
import os

def play():
   n=random.randint(0,len(hangman_words.word_list))

   word=hangman_words.word_list[n]
   # word='khandagale'
   lives=6
   word_size=len(word)


   print(hangman_arts.logo)
   # Challange 2 (A)
   # To fill dash in display accroding to word-size
   display= []
   while word_size!=0:
         display.append('_')
         word_size-=1

   print(hangman_arts.stages[lives])

   # Challange 3 
   # While loop will run till dash is present in display
   while '_' in display and lives!=0:
      # Challange 1
      print(f'{display.count('_')} letters left! \n\n{display}')
      guess=input("\nGuss a letter : ").lower()
      
      dupl=[]
      for index,letter in enumerate(word):
         if letter==guess:
            # save index of duplicate
            dupl.append(index)
      if dupl==[]:
         lives-=1 
         if lives==0:
            print(f'\nYou LOSE!{hangman_arts.stages[lives]}The word was {word} \n')
            choice()
            break
         # Challange 2 (B)
         # To replace dash with letter according to index
      for index in dupl:
         display[index]=guess
      print(hangman_arts.stages[lives])

   if lives>0:
     print(f'You WON! \nThe word was {word}')
     choice()



def choice():
   if input('Do you want to play HangMan : type "y" or "n" : ')=='y':
      os.system('cls')
      play()
   else:
      print('\nGood Bye\n')

choice()
