import art
import os

print(art.logo)
auction=[]

#This takes the input of bidders
choice=''
while choice!='no':
  name=input('What is your name? : ')
  bid=int(input('What is your bid?: $'))
  auction.append({'name':name,
                  'bid':bid,
  })
  choice=input('Are there any other bidders? Type \'yes or \'no\' : ')
  os.system('cls')

#This finds the highest bid!
highest_bid=0
for n in range(0,len(auction)):
  if highest_bid < auction[n]['bid']:
    highest_bid=auction[n]['bid']
    name=auction[n]['name']
 

print(f'The winner is {name} with a bid of ${highest_bid}')