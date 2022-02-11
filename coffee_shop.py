'''initial coffee shop resources'''
from data import resources
from order import process_order
from report import print_report


def _get_initial_resources():
    return resources.copy()


def _create_resources():
    initial_resources = _get_initial_resources()
    initial_resources['money'] = 0
    return initial_resources


def _ask_coffee_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def handle_customers():
    '''Handles customer requests, operates coffee shop'''
    choice = ''
    current_resources = _create_resources()

    while choice != 'off':
        choice = _ask_coffee_choice()

        if choice == 'report':
            print_report(current_resources)
        if choice in ('espresso', 'latte', 'cappuccino'):
            current_resources = process_order(
                resources=current_resources, order=choice)
        elif choice == 'off':
            pass
