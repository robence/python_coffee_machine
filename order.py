from data import MENU
from report import print_report


def process_order(resources, order):
    '''Handles incoming customer order'''
    missing_ingredient = _has_enough_ingredient(resources, order)

    if missing_ingredient != '':
        print(f"​Sorry there is not enough {missing_ingredient}.\n")
        return resources

    if _process_coins(order):
        remaining_resources = _process_transaction(resources, order)
    print(f"Here is your {order}. Enjoy!.\n")
    return remaining_resources


def _has_enough_ingredient(resources, order):
    item = _get_order_item(order)
    ingredients = item['ingredients']
    missing_ingredient = ''

    for ingredient, cost in ingredients.items():
        if cost > resources[ingredient]:
            missing_ingredient = ingredient
            break

    return missing_ingredient


def _process_coins(order):
    item = _get_order_item(order)
    money_cost = item['cost']
    money_inserted = True

    if money_inserted:
        print(f"{order} costs ${money_cost}.")
        return True

    print("Sorry that's not enough money. Money refunded.")
    return False


def _process_transaction(resources, order):
    print_report(resources=resources)

    item = _get_order_item(order)
    money_cost = item['cost']
    ingredients = item['ingredients']

    for ingredient, ingredient_cost in ingredients.items():
        resources[ingredient] -= ingredient_cost

    resources['money'] += money_cost

    print_report(resources=resources)
    return resources


def _get_order_item(order):
    return MENU[order]
