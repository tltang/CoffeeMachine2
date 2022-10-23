from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

lContinue = True
oCoffeeMaker = CoffeeMaker()
oMenu = Menu()
oPayment = MoneyMachine()

cItemList = oMenu.get_items()

while lContinue:
    cChoice = input(f"What would you like to order? {cItemList}: ")
    if cChoice == "off":
        lContinue = False
    elif cChoice == "report":
        oCoffeeMaker.report()
        oPayment.report()
    else:
        cMenuItem = oMenu.find_drink(cChoice)
        if cMenuItem is not None:
            if oCoffeeMaker.is_resource_sufficient(cMenuItem):
               if oPayment.make_payment(cMenuItem.cost):
                   oCoffeeMaker.make_coffee(cMenuItem)
