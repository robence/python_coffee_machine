from enum import Enum
from typing import Dict


class Resource(Enum):
    WATER = 'water'
    COFFEE = 'coffee'
    MILK = 'milk'
    MONEY = 'money'

    @staticmethod
    def from_str(label):
        if label == 'water':
            return Resource.WATER
        elif label == 'coffee':
            return Resource.COFFEE
        elif label == 'milk':
            return Resource.MILK
        elif label == 'money':
            return Resource.MONEY
        else:
            raise NotImplementedError


RESOURCE_NAMES: Dict[Resource, str] = {
    Resource.WATER: 'Water',
    Resource.MILK: 'Milk',
    Resource.COFFEE: 'Coffee',
    Resource.MONEY: 'Money',
}
