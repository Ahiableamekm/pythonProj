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

def resources_sufficient(order_ingredient):
    """Returns true if resouces is sufficent, False if not sufficient"""
    for item in order_ingredient:
        if order_ingredient[item]>= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
    

def process_coins():
    """Takes in the coins and returns total"""
    print('Please insert a coins!')
    total = int(input('How many quaters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

def transaction_sucessful(money_received, drink_cost):
    """Returns True for a sucessful transaction, False if not"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f'Here is ${change} dollars in change')
        global profit
        profit += drink_cost
        return True
    
    print("​Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(order_ingredient, drink_name):
    """Deduct the resources and makes the coffee"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}🍵. Enjoy")

machine_on = True
while machine_on:
    user_input = input('​What would you like? (espresso/latte/cappuccino): ')
    if user_input == 'off':
        machine_on = False
    elif user_input =='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if resources_sufficient(drink['ingredients']):
            payement = process_coins()
            if transaction_sucessful(payement, drink['cost']):
                make_coffee(drink['ingredients'], user_input)




        
