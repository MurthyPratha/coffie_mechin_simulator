from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mech=MoneyMachine()
maker=CoffeeMaker()


is_on=True

while is_on:
    drink=input(f"what would you like to drint {Menu().get_items()}: ").lower()
    if drink=="off":
        is_on=False
    elif drink=="report":
        maker.report()
        money_mech.report()
    else:    
        fd= Menu().find_drink(drink)
        if maker.is_resource_sufficient(fd) and money_mech.make_payment(fd.cost):
            maker.make_coffee(fd)
            
            


