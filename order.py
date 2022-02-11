from data import MENU
from report import print_report


def process_order(resources, order):
    missing_ingredient = _has_enough_ingredient(resources, order)

    if missing_ingredient != '':
        print(f"​Sorry there is not enough {missing_ingredient}.\n")
        return resources

    print_report(resources=resources)
    remaining_resources = _process_coins(resources, order)
    print_report(resources=remaining_resources)
    print(f"Here is your {order}. Enjoy!.\n")
    return remaining_resources


def _has_enough_ingredient(resources, order):
    item = MENU[order]
    ingredients = item['ingredients']
    missing_ingredient = ''

    for ingredient, cost in ingredients.items():
        if cost > resources[ingredient]:
            missing_ingredient = ingredient
            break

    return missing_ingredient


def _process_coins(resources, order):
    item = MENU[order]
    money_cost = item['cost']
    ingredients = item['ingredients']

    for ingredient, ingredient_cost in ingredients.items():
        resources[ingredient] -= ingredient_cost

    resources['money'] += money_cost

    return resources