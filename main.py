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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    '''loops threw menu and checks if value is greater than resource value and returns if order can be made and false if there's not enough '''
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f'sorry there is not enough {items}')
            return False
    return True

quarters = 0.25
dime = 0.10
nickel = 0.05
pennie = 0.01


def process_coins():
    """returns the total calculated"""
    print("please insert coins.")
    total = int(input('how much quarters?: ')) * quarters
    total += int(input("how many dimes?: ")) * dime
    total += int(input("how many nickels?: ")) * nickel
    total += float(input("how many pennies?: ")) * pennie
    return total


def is_transaction_successful(money_received,drink_cost):
    """return true when payment is accepted or false when money isn't enough"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print('sorry not enough money')
        return False

def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True#running while loop to continue

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino)')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]#pick a drink from the menu and type it into choice
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
