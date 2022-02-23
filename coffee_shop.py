'''initial coffee shop resources'''
from data import resources
from order import process_order
from report import print_report


def _ask_coffee_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


class CoffeeMaker:
    '''Operates Coffee Shop'''

    def __init__(self) -> None:
        self.resources = resources.copy()
        self.resources['money'] = 0

    def handle_customers(self):
        '''Handles customer requests, operates coffee shop'''
        choice = ''

        while choice != 'off':
            choice = _ask_coffee_choice()

            if choice == 'report':
                print_report(self.resources)
            if choice in ('espresso', 'latte', 'cappuccino'):
                self.resources = process_order(
                    resources=self.resources, order=choice)
            elif choice == 'off':
                pass

    def hello(self):
        '''Temp function'''
        print(self.__class__)
