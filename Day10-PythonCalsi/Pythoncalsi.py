import art
import os

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2


operations = {
  '+':add ,
  '-':sub ,
  '*':mul ,
  '/':div ,
}

def calculator():
  print(art.logo)
  n1=float(input('Whats the first no : '))
  choice=True
  while choice:
    for n in operations:
      print(f'=> {n}')
    symbol=input('Pick an operation from an above : ')

    n2=float(input('whats the second no : '))
    cal_function = operations[symbol]
    ans=cal_function(n1,n2)
    print(f'{n1} {symbol} {n2} = {ans}')
    if input(f'\nType \'y\' to continue calculating with {ans} or type \'n\' to start new calculation : ')=='y':
      n1=ans
      print(f'\nContinuing calculating with {n1}.')
    else:
      print('\n\nOk\n\n')
      choice=False
      os.system('cls')
      calculator()

calculator()
