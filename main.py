# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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



def calculate_resources(ingredients):

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True

def process_coins():

    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(payment,drink_cost):
    if payment >= drink_cost:
        global profit
        profit += payment
        change = round(payment-drink_cost,2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def coffee_machine_maker():
    is_coffee_machine_on = True

    while is_coffee_machine_on != False:

        coffee_options = input("What would you like ? (espresso/latte/cappuccino): ").lower()
        if coffee_options == "off":
            is_coffee_machine_on = False
            break
        elif coffee_options == "report":
            print(f"Water: {resources['water']} ml")
            print(f"Milk: {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} ml")
            print(f"Money: ${profit}")
        elif coffee_options == "espresso" or coffee_options == "latte" or coffee_options == "cappuccino":
            drink = MENU[coffee_options]
            if calculate_resources(drink['ingredients']):
                payment = process_coins()

                if is_transaction_successful(payment,drink['cost']):
                    make_coffee(coffee_options, drink["ingredients"])

        else:
            print("wrong choice selected!!! not practically possible in actual machine!!! ")







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coffee_machine_maker()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
