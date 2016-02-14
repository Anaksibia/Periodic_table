from enum import Enum

class Element:
    def __init__(self, number, name, symbol, period, group, atomic_mass, is_stable, discovery_year):
        def get_block(self):
            if self.group == 1 or self.group == 2 or self.symbol == 'He':
                return Element.Block.s
            elif 3 <= self.group <= 12:
                return Element.Block.d
            elif 13 <= self.group <= 18:
                return Element.Block.p
            else:
                return Element.Block.f

        self.number = number
        self.name = name
        self.symbol = symbol
        self.period = period
        self.group = group
        self.atomic_mass = atomic_mass
        self.is_stable = is_stable
        self.discovery_year = discovery_year
        self.block = get_block(self)

    def show(self, given_year):
        return self.discovery_year <= given_year

    class Block(Enum):
        s = 1
        d = 2
        p = 3
        f = 4

