import random

import item as i
from random import Random


class Actor:
    def __init__(self, name, x, y, s, d, h, c, hp, sp):
        self.equipment = []
        self.alive = True
        self.name = name
        self.strength = s
        self.defence = d
        self.hand_to_hand_combat = h
        self.critic_attack = c
        self.health = hp
        self.speed = sp
        self.y = y
        self.x = x
        self.attacking_distance = 4

    def get_name(self):
        return self.name

    def check_health(self):
        return self.health

    def change_live_status(self):
        self.alive = False

    def is_alive(self):
        return self.alive

    def change_health(self, num):
        self.health += num

    def apply_equipment_effects(self):
        for element in self.equipment:
            if isinstance(element, i.Weapon):
                self.strength += element.attack
            if isinstance(element, i.Armor):
                self.defence += element.defence

    def get_damage_from_weapon(self):
        for element in self.equipment:
            if element.type == "weapon":
                return element.attack
        return 0

    def calculate_damage(self):
        sum = self.strength + self.get_damage_from_weapon() + random.randrange(0, 20) + self.critic_attack;
        return sum

    def attack(self, opponent):
        op_health = opponent.check_health()
        damage = self.calculate_damage()
        if max(0, op_health - damage) == 0:
            opponent.change_live_status()
            #print(f"umiera {opponent.name}")
            return False
        else:
            opponent.change_health(-damage)
            #print(f"oponent {opponent.name} zyje ale ma ", opponent.check_health(), "hp")
            return True

class Person(Actor):
    def __init__(self, name, x, y, s, d, h, c, hp, sp):
        super().__init__(name, x, y, s, d, h, c, hp, sp)
        self.visibility = 1
        self.character = "@"

    def add_to_eq(self, item):
        self.equipment.append(item)


class Mob(Actor):
    def __init__(self, type_of_mob, name, x, y, s, d, h, c, hp, sp):
        super().__init__(name, x, y, s, d, h, c, hp, sp)
        self.type_of_mob = type_of_mob
        self.character = "%"
