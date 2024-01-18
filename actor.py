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
        self.attacking_distance = 1

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

    def attack(self, opponent, flag,sdscr):
        op_health = opponent.check_health()
        damage = self.calculate_damage() - opponent.defence
        if opponent.agility >= random.randint(0, 100):
            if flag:
                sdscr.addstr(f"{opponent.name} zrobił unik!")
            return True
        if max(0, op_health - damage) == 0:
            opponent.change_live_status()
            if flag:
                sdscr.addstr(f"{self.name} zadaje: {damage} obrażeń, umiera {opponent.name}")
            return False
        else:
            if damage < 0:
                if flag:
                    sdscr.addstr("Atak został zablokowany")
                    return True
            else:
                opponent.change_health(-damage)
                if flag:
                    sdscr.addstr(f"{self.name} zadaje: {damage} obrażeń, {opponent.name} zyje ale ma "
                                 f"{opponent.check_health()} hp")
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

    def take_off_from_eq(self, num):
        self.equipment[num].take_of_item_effect(self)
        self.equipment[num].put_on = False
        self.equipment.pop(num)

    def show_backpack(self, stdscr):
        stdscr.addstr(f"W plecaku posiadasz: \n")
        index = 0
        for elements in self.backpack:
            stdscr.addstr(f"{index}:{elements.name}\n")
            index += 1

    def show_eq(self, stdscr):
        stdscr.addstr(f"Oto twój ekwipunek: \n")
        index = 0
        for elements in self.equipment:
            stdscr.addstr(f"{elements.type}:{elements.name}\n")
            index += 1
        self.show_backpack(stdscr)

    def equipment_display(self,msg_window,stdscr):
        self.show_eq(msg_window)
        msg_window.addstr("Aby założyć przedmiot podaj jego numer!\n")
        msg_window.refresh()
        response = stdscr.getkey()
        if (response != '\x1b'):
            try:
                item_number = int(response)
                if 0 <= item_number < 6:
                    msg_window.addstr(f"Wybrałeś {self.backpack[item_number].name}. Wcisnij enter aby potwierdzić.")
                    msg_window.refresh()
                    confirm = stdscr.getkey()

                    if confirm == "\n":  # Check if Enter is pressed
                        self.add_to_eq(item_number)
                        msg_window.addstr(f"Przedmiot dodany do ekwipunku. ")
                    else:
                        msg_window.addstr(f"Anulowano dodawanie przedmiotu. ")
                else:
                    msg_window.addstr("Niepoprawny numer przedmiotu. ")
            except ValueError:
                msg_window.addstr("Niepoprawny format. Podaj numer przedmiotu. ")
        else:
            msg_window.refresh()


class Mob(Actor):
    def __init__(self, type_of_mob, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.type_of_mob = type_of_mob
        self.character = "%"
