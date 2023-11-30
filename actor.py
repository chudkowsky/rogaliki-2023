import random


class Actor:
    def __init__(self, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        self.equipment = []
        self.alive = True
        self.name = name
        self.strength = strength
        self.defence = defence
        self.hand_to_hand_combat = hand_to_hand_combat
        self.critic_attack = critical_attack
        self.health = hp
        self.agility = agility
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
            if not element.put_on:
                if element.type == "weapon":
                    self.strength += element.attack
                if element.type == "armor":
                    self.defence += element.defence
                element.put_on = True
            else:
                print(f"{element.name} already equiped!")

    def get_damage_from_weapon(self):
        for element in self.equipment:
            if element.type == "weapon":
                return element.attack
        return 0

    def calculate_damage(self):
        return (self.strength + self.get_damage_from_weapon() + random.randrange(0, 20) +
                random.randrange(0, 5) * self.critic_attack)

    def attack(self, opponent, flag):
        op_health = opponent.check_health()
        damage = self.calculate_damage() - opponent.defence
        if opponent.agility >= random.randint(0, 100):
            if flag:
                print(f"{opponent.name} zrobił unik!")
            return True
        if max(0, op_health - damage) == 0:
            opponent.change_live_status()
            if flag:
                print(f"{self.name} zadaje: {damage} obrażeń, umiera {opponent.name}")
            return False
        else:
            if damage < 0:
                if flag:
                    print("Atak został zablokowany")
                    return True
            else:
                opponent.change_health(-damage)
                if flag:
                    print(f"{self.name} zadaje: {damage} obrażeń, {opponent.name} zyje ale ma",
                          opponent.check_health(), "hp")
            return True


class Person(Actor):
    def __init__(self, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.visibility = 1
        self.character = "@"

    def add_to_eq(self, item):
        self.equipment.append(item)
        self.apply_equipment_effects()


class Mob(Actor):
    def __init__(self, type_of_mob, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.type_of_mob = type_of_mob
        self.character = "%"
