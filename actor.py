import map
class Actor:
    def __init__(self, name):
        self.name = name
        self.atack = 1
        self.defence = 1
        self.critic_atack = 1
        self.health = 100
        self.speed = 1
        self.y = 0
        self.x = 0

    def get_name(self):
        return self.name


class Person(Actor):
    def __init__(self):
        self.visibility = 1
        self.equipment = list

    def add_to_eq(self, item):
        self.equipment.append(item)


class Mob(Actor):
    def __init__(self, type_of_mob):
        self.weapon = 0
        self.type_of_mob = type_of_mob
