class Item:
    def __init__(self, x, y, quality,name,):
        self.name = name
        self.character = '&'
        self.x = x
        self.y = y
        self.quality = quality
        self.put_on = False

    def apply_item_effect(self, actor):
        raise NotImplementedError


class Weapon(Item):
    def __init__(self, x, y,  quality,name , attack):
        super().__init__(x, y, quality,name, )
        self.attack = attack * self.quality.value[1]
        self.type = "weapon"

    def apply_item_effect(self, actor):
        actor.strength += self.attack


class Armor(Item):
    def __init__(self, x, y, quality, name, defence):
        super().__init__(x, y, quality, name)
        self.defence = defence * self.quality.value[1]
        self.type = "armor"

    def apply_item_effect(self, actor):
        actor.defence += self.defence


class Potion(Item):
    def __init__(self, x, y, quality, name, power, ):
        super().__init__(x, y, quality, name)
        self.power = power * self.quality.value[1]
        self.type = "Potion"

    def drink_potion(self, actor):
        raise NotImplementedError


class HealingPotion(Potion):
    def __init__(self, x, y, quality, name, power):
        super().__init__(x, y, quality, name, power)
        self.power = power * self.quality.value[1]
        self.type = "Potion"

    def drink_potion(self, actor):
        actor.health += self.power

class PotionOfStrength(Potion):
    def __init__(self, x, y, quality, name, power):
        super().__init__(x, y, quality, name, power)
        self.power = power * self.quality.value[1]
        self.type = "Potion"

    def drink_potion(self, actor):
        actor.strength += self.power
