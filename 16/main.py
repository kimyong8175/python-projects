from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def main():
    drink_menu = Menu()
    coffee_maker = CoffeeMaker()
    payment = MoneyMachine()

    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            payment.report()
        else:
            drink = drink_menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if payment.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
