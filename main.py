'''Start serving customers'''
from coffee_shop import CoffeeMaker


def main():
    '''Operates Coffee Shop'''
    coffee_maker = CoffeeMaker()
    coffee_maker.handle_customers()


main()
