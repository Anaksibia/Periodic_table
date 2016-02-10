import re
from codecs import open

from elements_class import Element


class Table:
    def __init__(self):
        self.elements = []
        regex = r'\[?(\d+,?\d*)'
        with open("cgi-bin/elements.csv", encoding='utf-8') as fin:
            for line in fin:
                parameters = line.split(sep=';')
                number = int(parameters[0])
                name = parameters[1]
                symbol = parameters[2]
                if len(parameters[4]) > 1:
                    period_group = parameters[4].split(sep=',')
                    period = int(period_group[0])
                    group = int(period_group[1])
                else:
                    period = int(parameters[4])
                    group = 20   # group not identified
                if parameters[5][0] == '[':
                    atomic_mass = re.search(regex, parameters[5]).group(0)[1:]
                    stability = False
                else:
                    atomic_mass = re.search(regex, parameters[5]).group(0)
                    stability = True
                if ',' in atomic_mass:
                    atomic_mass = float('.'.join(atomic_mass.split(sep=',')))
                else:
                    atomic_mass = int(atomic_mass)
                discovery_year = int(parameters[6])
                self.elements.append(Element(number, name, symbol, period, group, atomic_mass, stability, discovery_year))

    def get_discovered_elements(self, given_year):
        discovered_elements = []
        for element in self.elements:
            if element.show(given_year):
                discovered_elements.append(element)
        return discovered_elements

    def get_lantanoids(self):
        lantanoids = []
        for element in self.elements:
            if element.group == 20 and element.period == 6:
                lantanoids.append(element)
        return lantanoids

    def get_actinoids(self):
        actinoids = []
        for element in self.elements:
            if element.group == 20 and element.period == 7:
                actinoids.append(element)
        return actinoids

    def get_ordinary_elements(self):
        ordinary_elements = []
        for element in self.elements:
            if element.group != 20:
                ordinary_elements.append(element)
        return ordinary_elements
