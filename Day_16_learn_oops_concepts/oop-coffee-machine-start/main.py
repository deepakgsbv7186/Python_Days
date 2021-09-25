from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # check for the resources
        if coffee_maker.is_resource_sufficient(drink):
            # ask for the money required
            # check for the successfull transaction
            if money_machine.make_payment(drink.cost):
                # now make coffee and update resources 
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry we run out of resources")

