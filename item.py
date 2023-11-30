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
        self.attack = attack*self.quality.value[1]
        self.type = "weapon"


class Armor(Item):
    def __init__(self, x, y, quality,defence):
        super().__init__(x, y,quality)
        self.defence = defence*self.quality.value[1]
        self.type = "armor"


'''
class Potion(Item):
    raise NotImplementedError


class Ring(Item):
    raise NotImplementedError


class EnchantingBook(Item):
    raise NotImplementedError
'''
