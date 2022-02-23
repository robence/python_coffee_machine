'''initial coffee shop resources'''
from data import resources
from order import process_order
from report import print_report


class CoffeeMaker:
    '''Operates Coffee Shop'''

    def __init__(self) -> None:
        self.resources = resources.copy()
        self.resources['money'] = 0

    def _ask_coffee_choice(self):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        return choice

    def handle_customers(self):
        '''Handles customer requests, operates coffee shop'''
        choice = ''

        while choice != 'off':
            choice = self._ask_coffee_choice()

            if choice == 'report':
                print_report(self.resources)
            if choice in ('espresso', 'latte', 'cappuccino'):
                self.resources = process_order(
                    resources=self.resources, order=choice)
            elif choice == 'off':
                pass
