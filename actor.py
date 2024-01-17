import random


class Actor:
    def __init__(self, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        self.equipment = []
        self.backpack = []
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
        for item in self.equipment:
            if not item.put_on:
                item.apply_item_effect(self)
                item.put_on = True

    def calculate_damage(self):
        return (self.strength + random.randrange(0, 20) + self.hand_to_hand_combat +
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

    def add_to_backpack(self, item):
        self.backpack.append(item)

    def add_to_eq(self, num):
        it = self.backpack.pop(num)
        self.equipment.append(it)
        self.apply_equipment_effects()


    def show_backpack(self, stdscr):
        pos_x = 5
        pos_y = 40
        stdscr.addstr(pos_x, pos_y, f" W plecaku posiadasz: \n")
        for elements in self.backpack:
            pos_x += 1
            stdscr.addstr(pos_x, pos_y, f"-{elements.name}")


class Mob(Actor):
    def __init__(self, type_of_mob, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.type_of_mob = type_of_mob
        self.character = "%"
