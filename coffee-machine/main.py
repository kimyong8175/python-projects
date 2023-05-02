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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources):
    print(
        f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${profit}"""
    )


def is_resource_sufficient(oreder_ingredient):
    """
    Returs True when order can be made, False if ingredients is not sufficient
    """
    for item in oreder_ingredient:
        if oreder_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def press_coins():
    """
    Returns total calculated from coin inserted.
    """
    total = 0
    print("Please insert coins.")
    total += int(input("How many pennies: ")) * 0.01
    total += int(input("How many quaters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05

    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Returns True when the payments is accepted, False if money is not sufficient
    """
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, oreder_ingredient):
    for item in oreder_ingredient:
        resources[item] -= oreder_ingredient[item]
    print(f"Here is your {drink_name}.")


def main():
    is_on = True
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        if user_choice == "off":
            break
        elif user_choice == "report":
            print_report(resources)
        else:
            drink = MENU[user_choice]
            if is_resource_sufficient(drink["ingredients"]):
                inserted_coins = press_coins()
                if is_transaction_successful(inserted_coins, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])


if __name__ == "__main__":
    main()
