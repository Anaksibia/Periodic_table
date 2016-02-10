from enum import Enum

class Block(Enum):
    block_s = 1
    block_d = 2
    block_p = 3
    block_f = 4


def get_block(self):
    if self.period <= 7 and (self.group == 1 or self.group == 2):
        return Block(1)
    elif self.period <= 7 and 3 <= self.group <= 12:
        return Block(2)
    elif self.period <= 7 and 13 <= self.group <= 18:
        return Block(3)
    else:
        return Block(4)


class Element:
    def __init__(self, number, name, symbol, period, group, atomic_mass, discovery_year):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.period = period
        self.group = group
        self.atomic_mass = atomic_mass
        self.discovery_year = discovery_year
        self.block = get_block(self)

H = Element(1, "hhh", "H", 1, 1, 1, 200)
C = Element(7, "sdf", "C", 5, 7, 12, 1200)
W = Element(18, "sdf", "W", 3, 18, 234, 1500)
WW = Element(74, "sdf", "WW", 7, None, 23, 2000)

S = [H, C, W, WW]
for elem  in S:
    print(elem.block)