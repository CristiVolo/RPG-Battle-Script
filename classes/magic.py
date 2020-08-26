import random


# The class that holds all the details about a spell
class Spell:    # !Remember: self = instance of the class
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_spell_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)