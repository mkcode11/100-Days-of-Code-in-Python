MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def makecoffee(drink):
    resources["water"]-=MENU[drink]['ingredients']['water']
    if drink=='cappuccino' or drink=='latte':
        resources["milk"]-=MENU[drink]['ingredients']['milk']
    resources["coffee"]-=MENU[drink]['ingredients']['coffee']
    return f'Here is your {drink}. Enjoy!'

profit=0
def is_transaction_successful(drink,money):
    cost=MENU[drink]['cost']
    if money>=cost:
        global profit
        profit+=cost
        if money>cost:
            formated_money='{:.2f}'.format(money-cost)
            print(f'\nHere is ${formated_money} dollars in change.')
        return True
    else:
        print('\nSorry that\'s not enough money. Money refunded.')
        return False
        

def is_resources_sufficient(drink):
    n=0
    stock=MENU[drink]['ingredients']
    for items in stock:
        if resources[items]>=stock[items]:
           n+=1 
        else:
            print(f'\nSorry there is not enough {items}.')
            return False
    if n==2 or n==3:
        return True


def processCoins():

    quarters=int(input('Please insert coins.\nhow many quarters?: '))
    dimes=int(input('how many dimes?: '))
    nickles=int(input('how many nickles?: '))
    pennies=int(input('how many pennies?: '))

    total_money=(0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    return total_money

def ask():

    is_off=False
    while not is_off:
        order=input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()
        if order=='report':
            print(f'\n<>REPORT<>\n->Water:{resources['water']}ml\n->Milk:{resources["milk"]}ml\n->Coffee:{resources["coffee"]}g\n->Money:${profit}')
        elif order=='off':
            print('\nGood Bye.\n')
            is_off=True
        elif order=='refill':
            resources['water']=300
            resources['milk']=200
            resources['coffee']=100
            print(f'\n<>REFILL<>\n->Water:{resources['water']}ml\n->Milk:{resources["milk"]}ml\n->Coffee:{resources["coffee"]}g\n->Money:${profit}')
        elif order=='espresso'or order=='cappuccino'or order=='latte':
            if is_resources_sufficient(order):
                if is_transaction_successful(order,processCoins()):
                    print(makecoffee(order))
        else:
            print('Invalid input')  
            

ask() 
