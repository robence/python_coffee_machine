'''Importing Enum to create a Resource instead of using strings'''
from enum import Enum
from typing import Dict


class Resource(Enum):
    '''Contains two-way casting for resource object'''
    WATER = 'water'
    COFFEE = 'coffee'
    MILK = 'milk'
    MONEY = 'money'

    @staticmethod
    def from_str(label):
        '''Creates a Resource object from string'''
        if label == 'water':
            return Resource.WATER
        if label == 'coffee':
            return Resource.COFFEE
        if label == 'milk':
            return Resource.MILK
        if label == 'money':
            return Resource.MONEY
        raise NotImplementedError


RESOURCE_NAMES: Dict[Resource, str] = {
    Resource.WATER: 'Water',
    Resource.MILK: 'Milk',
    Resource.COFFEE: 'Coffee',
    Resource.MONEY: 'Money',
}
