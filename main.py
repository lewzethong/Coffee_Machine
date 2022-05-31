from data import MENU, resources


def enough_ingredient(drinks):
    for ingredient in MENU[drinks]['ingredients']:
        if resources[ingredient] < MENU[drinks]['ingredients'][ingredient]:
            print(f"insufficient {ingredient}, unable to select option")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coin():
    total = 0
    print("Please insert coins.")
    total += int(input('How many quarters?:')) * 0.25
    total += int(input('How many dimes?:')) * 0.10
    total += int(input('How many nickels?:')) * 0.05
    total += int(input('How many pennies?:')) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

operate = True
profit = 0
while operate:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == 'off':
        operate = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_ingredient(choice):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])