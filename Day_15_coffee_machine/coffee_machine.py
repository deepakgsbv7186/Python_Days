import os
# coffee resources
machine_inventory = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0,
}
incredients_needed = [
    {
        "name" : "Espresso",
        "water" : 50,
        "milk" : 0,
        "coffee" : 18,
        "price" : 1.50,
    },
    {
        "name" : "Latte",
        "water" : 200,
        "milk" : 150,
        "coffee" : 24,
        "price" : 2.50,
    },
    {
        "name" : "Cappuccino",
        "water" : 250,
        "milk" : 100,
        "coffee" : 24,
        "price" : 3.00,
    },
]
def report():
    print("\n**** Inventory Available ****")
    print(f"Water: {machine_inventory['water']}")
    print(f"Milk: {machine_inventory['milk']}")
    print(f"Coffee: {machine_inventory['coffee']}")
    print(f"Money: {machine_inventory['money']}")


# check the inventory (sufficient incredients for the coffee request)
def is_incredients_sufficient(choice):
    """ compare the user coffee choice requirments to meet the inventory"""
    choice -= 1
    apology = "Sorry, We Don't have enough inventory!!!"
    coffee_name = incredients_needed[choice]["name"]
    water = incredients_needed[choice]["water"]
    milk = incredients_needed[choice]["milk"]
    coffee = incredients_needed[choice]["coffee"]
    price = incredients_needed[choice]["price"]
    # print(f"{coffee_name} {water} {milk} {coffee}")
    if machine_inventory["water"] >= water :
        if machine_inventory["milk"] >= milk :
            if machine_inventory["coffee"] >= coffee :
                print("Please Inserted Money\n")
                # call function collect()
                money = collect_money()
                if check_transaction(money,price):
                    # make the coffee
                    machine_inventory["water"] -= water
                    machine_inventory["milk"] -= milk
                    machine_inventory["coffee"] -= coffee
                    print(f"Enjoy Your {coffee_name}")
            else:
                print(f"{apology}")
        else:
            print(f"{apology}")
    else:
        print(f"{apology}")


# process money ( 1 paisa = ₹ 0.01, 5 paisa = ₹ 0.05, 10 paisa = ₹ 0.10, 25 paisa = ₹ 0.25)
def collect_money():
    _1paise = int(input("1 paise: "))
    _5paise = int(input("5 paise: "))
    _10paise = int(input("10 paise: "))
    _25paise = int(input("25 paise: "))

    user_money = (0.01 * _1paise) + (0.05 * _5paise) + (0.10 * _10paise) + (0.25 * _25paise)
    return user_money

# check for successful transactions
def check_transaction(user_money,actual_price):
    if user_money >= actual_price:
        # return extra money
        return_amount = round(user_money - actual_price, 2)
        print(f"Please Collect Your Change: {return_amount}")
        # add money to inventory
        machine_inventory["money"] += actual_price
        return True
    else:
        print(f"Insufficent Money!!!\nReturned: ₹{user_money}")
        return False

machine = True
while machine:
    # ask user for coffee selection
    coffee_choice = input("What would you like?\n( 1->Espresso 2->Latte 3->Cappuccino )\nOption: ")
    if coffee_choice == 'report':
        report()
    elif coffee_choice == 'off':
        machine = False
    else:
        os.system("cls")
        # check for the incredients
        coffee_choice = int(coffee_choice)
        is_incredients_sufficient(coffee_choice)
