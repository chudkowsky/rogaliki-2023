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
    def take_of_item_effect(self,actor):
        raise NotImplementedError

class Weapon(Item):
    def __init__(self, x, y,  quality,name , attack):
        super().__init__(x, y, quality,name, )
        self.power = attack * self.quality.value[1]
        self.type = "weapon"


    def apply_item_effect(self, actor):
        actor.strength += self.power

    def take_of_item_effect(self,actor):
        actor.strength -= self.power




class Armor(Item):
    def __init__(self, x, y, quality, name, defence):
        super().__init__(x, y, quality, name)
        self.power = defence * self.quality.value[1]
        self.type = "armor"

    def apply_item_effect(self, actor):
        actor.defence += self.power

    def take_of_item_effect(self,actor):
        actor.defence -= self.power

class Gloves(Item):
    def __init__(self, x, y, quality, name, hand_to_hand_combat):
        super().__init__(x, y, quality, name)
        self.power = hand_to_hand_combat * self.quality.value[1]
        self.type = "gloves"

    def apply_item_effect(self, actor):
        actor.hand_to_hand_combat += self.power

    def take_of_item_effect(self,actor):
        actor.hand_to_hand_combat -= self.power

class Boots(Item):
    def __init__(self, x, y, quality, name, agility):
            super().__init__(x, y, quality, name)
            self.power = agility* self.quality.value[1]
            self.type = "Boots"

    def apply_item_effect(self, actor):
            actor.agility += self.power

    def take_of_item_effect(self, actor):
            actor.agility -= self.power

class Potion(Item):
    def __init__(self, x, y, quality, name, power, ):
        super().__init__(x, y, quality, name)
        self.power = power * self.quality.value[1]
        self.type = "Potion"



class HealingPotion(Potion):
    def __init__(self, x, y, quality, name, power):
        super().__init__(x, y, quality, name, power)
        self.power = power * self.quality.value[1]
        self.type = "Potion"

    def apply_item_effect(self, actor):
        actor.health += self.power

class PotionOfStrength(Potion):
    def __init__(self, x, y, quality, name, power):
        super().__init__(x, y, quality, name, power)
        self.power = power * self.quality.value[1]
        self.type = "Potion"

    def apply_item_effect(self, actor):
        actor.strength += self.power
