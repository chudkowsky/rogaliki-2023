from enum import Enum


class Item:
    def __init__(self, x, y, quality):
        self.character = '&'
        self.x = x
        self.y = y
        self.quality = quality


class Weapon(Item):
    def __init__(self,x, y, quality, attack):
        super().__init__(x, y,quality)
        self.attack = attack*quality.value[1]
        self.type = "weapon"


class Armor(Item):
    def __init__(self, x, y, defence, type):
        super().__init__(x, y)
        self.defence = defence
        self.type = type


'''
class Potion(Item):
    raise NotImplementedError


class Ring(Item):
    raise NotImplementedError


class EnchantingBook(Item):
    raise NotImplementedError
'''
