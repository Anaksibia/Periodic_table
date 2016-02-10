from enum import Enum

class Block(Enum):
    s = 1
    d = 2
    p = 3
    f = 4

def get_block(self):
    if self.group == 1 or self.group == 2 or self.symbol == 'He':
        return Block(1)
    elif 3 <= self.group <= 12:
        return Block(2)
    elif 13 <= self.group <= 18:
        return Block(3)
    else:
        return Block(4)


class Element:
    def __init__(self, number, name, symbol, period, group, atomic_mass, stability, discovery_year):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.period = period
        self.group = group
        self.atomic_mass = atomic_mass
        self.stability = stability
        self.discovery_year = discovery_year
        self.block = get_block(self)


    def show(self, given_year):
        return self.discovery_year <= given_year

