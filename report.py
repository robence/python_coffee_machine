from resource import RESOURCE_NAMES, Resource
from typing import Dict


def _create_resource_suffix(resource_enum, value):
    if resource_enum == Resource.MILK or resource_enum == Resource.WATER:
        return f'{value}ml'
    if resource_enum == Resource.COFFEE:
        return f'{value}g'
    if resource_enum == Resource.MONEY:
        return f'${value}'
    return ''


def _print_resource(resource, value):
    resource_enum = Resource.from_str(resource)

    resource_suffix = _create_resource_suffix(resource_enum, value)
    resource_name = RESOURCE_NAMES[resource_enum]
    print(f"{resource_name}: {resource_suffix}")


def print_report(resources: Dict[str, float]):
    print("")
    for resource, value in resources.items():
        _print_resource(resource, value)
    print("")
