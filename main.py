from data import MENU, resources
from order import process_order
from report import print_report


def create_resources():
    initial_resources = resources.copy()
    initial_resources['money'] = 0
    return initial_resources


def ask_coffee_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def handle_customers():
    choice = ''
    current_resources = create_resources()

    while choice != 'off':
        choice = ask_coffee_choice()

        if choice == 'report':
            print_report(current_resources)
        if (choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
            current_resources = process_order(
                resources=current_resources, order=choice)
        elif choice == 'off':
            pass


def main():
    handle_customers()


main()
