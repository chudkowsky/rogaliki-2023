class Item:
    def __init__(self, x, y, quality,name):
        self.name = name
        self.character = '&'
        self.x = x
        self.y = y
        self.quality = quality
        self.put_on = False


class Weapon(Item):
    def __init__(self, x, y, quality, attack,name):
        super().__init__(x, y, quality,name)
        self.attack = attack * self.quality.value[1]
        self.type = "weapon"


class Armor(Item):
    def __init__(self, x, y, quality, defence,name):
        super().__init__(x, y, quality,name)
        self.defence = defence * self.quality.value[1]
        self.type = "armor"


'''
class Potion(Item):
    raise NotImplementedError


class Ring(Item):
    raise NotImplementedError


class EnchantingBook(Item):
    raise NotImplementedError
'''
