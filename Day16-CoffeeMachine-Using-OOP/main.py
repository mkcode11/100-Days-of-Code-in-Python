from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
coffee=CoffeeMaker()
money=MoneyMachine()
is_off=False

while not is_off :
    order=input(f'What would you like to order ({menu.get_items()}) : ')
    if order=='report':
        coffee.report()
        money.report()
    elif order=='off':
        is_off=True
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
           
   
