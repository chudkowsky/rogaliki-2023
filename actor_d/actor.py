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
        self.lvl = 1

    def get_name(self):
        return self.name

    def check_health(self):
        return self.health

    def level_up(self):
        self.strength += 3
        self.defence += 3
        self.hand_to_hand_combat += 3
        self.critic_attack += 3
        self.agility += 3
        self.lvl += 1
        self.health = 100

    def change_live_status(self, map):
        x = self.x
        y = self.y
        item = self.drop_eq_when_died()
        if (item != None):
            item.y = y
            item.x = x
            map.items.append(item)
        self.alive = False

    def drop_eq_when_died(self):
        if self.equipment:
            self.equipment[0].take_of_item_effect(self)
            return self.equipment.pop(0)
        else:
            return None

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

    def attack(self, opponent, flag, sdscr, map):
        op_health = opponent.check_health()
        damage = self.calculate_damage() - opponent.defence
        if opponent.agility >= random.randint(0, 100):
            if flag:
                sdscr.addstr(f"{opponent.name} zrobił unik!\n")
            return True
        if max(0, op_health - damage) == 0:
            opponent.change_live_status(map)
            if flag:
                sdscr.addstr(f"{self.name} zadaje: {damage} obrażeń, umiera {opponent.name}\n")
            return False
        else:
            if damage < 0:
                if flag:
                    sdscr.addstr("Atak został zablokowany\n")
                return True
            else:
                opponent.change_health(-damage)
                if flag:
                    sdscr.addstr(f"{self.name} zadaje: {damage} obrażeń, {opponent.name} zyje ale ma "
                                 f"{opponent.check_health()} hp\n")
                return True


class Person(Actor):
    def __init__(self, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.visibility = 1
        self.character = "@"

    def add_to_backpack(self, item):
        self.backpack.append(item)

    def add_to_eq(self, num):
        item_type = self.backpack[num].type

        for index, equipped_item in enumerate(self.equipment):
            if equipped_item.type == item_type:
                self.take_off_from_eq(index)

        it = self.backpack.pop(num)
        self.equipment.append(it)
        self.apply_equipment_effects()

    def take_off_from_eq(self, num):
        self.equipment[num].take_of_item_effect(self)
        self.equipment[num].put_on = False
        self.add_to_backpack(self.equipment.pop(num))

    def show_backpack(self, stdscr):
        stdscr.addstr(f"W plecaku posiadasz: \n\n")
        index = 0
        for elements in self.backpack:
            stdscr.addstr(f"{index}:{elements.name}:{elements.power}\n")
            index += 1

    def show_eq(self, stdscr):
        equipment_types = {"armor": False, "weapon": False, "gloves": False, "boots": False}

        stdscr.addstr("Oto twój ekwipunek: \n\n")

        for element in self.equipment:
            equipment_types[element.type] = True
            stdscr.addstr(f"{element.type.capitalize()}:{element.name}:{element.power}+ \n")

        for equipment_type, is_empty in equipment_types.items():
            if not is_empty:
                stdscr.addstr(f"{equipment_type.capitalize()} : empty\n")

        stdscr.addstr("\n")

    def equipment_display(self, msg_window, stdscr):
        self.show_backpack(msg_window)
        msg_window.addstr("\nAby założyć przedmiot podaj jego numer!\n")
        msg_window.refresh()
        response = stdscr.getkey()
        if response != '\x1b':
            try:
                item_number = int(response)
                if 0 <= item_number < len(self.backpack):
                    msg_window.addstr(f"Wybrałeś {self.backpack[item_number].name}. Wcisnij enter aby potwierdzić.")
                    msg_window.refresh()
                    confirm = stdscr.getkey()

                    if confirm == "\n":  # Check if Enter is pressed
                        if (self.backpack[item_number].type != "potion"):
                            self.add_to_eq(item_number)
                            msg_window.addstr(f"Przedmiot dodany do ekwipunku. \n")
                        else:
                            self.backpack[item_number].apply_item_effect(self)
                            self.backpack.pop(item_number)
                            msg_window.addstr(f"Wypito miksture. ")
                    else:
                        msg_window.addstr(f"Anulowano dodawanie przedmiotu. ")
                else:
                    msg_window.addstr("Niepoprawny numer przedmiotu. ")
            except ValueError:
                msg_window.addstr("Niepoprawny format. Podaj numer przedmiotu. ")
        else:
            msg_window.refresh()

    def within_attacking_distance(self, map):
        player_position = (map.actor.x, map.actor.y)
        attacking_distance = map.actor.attacking_distance
        opponents = []

        for i in range(1, 1 + attacking_distance):
            if map.map_check_mobs(player_position[0] + i, player_position[1])[0]:
                elem = map.map_check_mobs(player_position[0] + i, player_position[1])[1]
                opponents.append((elem, "down"))

            if map.map_check_mobs(player_position[0] - i, player_position[1])[0]:
                elem = map.map_check_mobs(player_position[0] - i, player_position[1])[1]
                opponents.append((elem, "up"))

            if map.map_check_mobs(player_position[0], player_position[1] + i)[0]:
                elem = map.map_check_mobs(player_position[0], player_position[1] + i)[1]
                opponents.append((elem, "right"))

            if map.map_check_mobs(player_position[0], player_position[1] - i)[0]:
                elem = map.map_check_mobs(player_position[0], player_position[1] - i)[1]
                opponents.append((elem, "left"))

        if opponents:
            return [True, opponents]
        else:
            return [False, None]

    def attack_with_key(self, mapka, mobs_killed, msg_window, direction):
        tmp = mapka.actor.within_attacking_distance(mapka)
        if tmp[0]:
            for elem in tmp[1]:
                if direction == "down":
                    if elem[1] == "down":
                        if not (mapka.actor.attack(elem[0], 1, msg_window, mapka)):
                            mobs_killed += 1
                        msg_window.refresh()
                elif direction == "up":
                    if elem[1] == "up":
                        if not (mapka.actor.attack(elem[0], 1, msg_window, mapka)):
                            mobs_killed += 1
                        msg_window.refresh()
                elif direction == "left":
                    if elem[1] == "left":
                        if not (mapka.actor.attack(elem[0], 1, msg_window, mapka)):
                            mobs_killed += 1
                        msg_window.refresh()
                elif direction == "right":
                    if elem[1] == "right":
                        if not (mapka.actor.attack(elem[0], 1, msg_window, mapka)):
                            mobs_killed += 1

                        msg_window.refresh()
        return mobs_killed


class Mob(Actor):
    def __init__(self, type_of_mob, name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility):
        super().__init__(name, x, y, strength, defence, hand_to_hand_combat, critical_attack, hp, agility)
        self.type_of_mob = type_of_mob
        self.character = "%"
        self.health_copy = hp
        self.vision = 5
        self.last_known_player_pos = None

    def within_attacking_distance(self, map):
        player_position = (map.actor.x, map.actor.y)
        attacking_distance = 1
        for i in range(1, 2):
            if player_position[0] == self.x and abs(player_position[1] - self.y) <= attacking_distance:
                return True
            if player_position[1] == self.y and abs(player_position[0] - self.x) <= attacking_distance:
                return True
        return False

    def within_the_vision(self, map):
        player_position = (map.actor.x, map.actor.y)
        vision = self.vision
        for i in range(1, 2):
            if player_position[0] == self.x and abs(player_position[1] - self.y) <= vision:
                return True
            if player_position[1] == self.y and abs(player_position[0] - self.x) <= vision:
                return True
        return False

    def move_mob(self, x1, y1, map):
        print(f"Moving mob {self.name} to ({x1}, {y1})")
        if map.if_move_possible(x1, y1):
            self.x = x1
            self.y = y1
        else:
            print("move not possible")

    def make_move(self, map, msg_window):
        if self.within_attacking_distance(map):
            self.attack(map.actor, 1, msg_window, map)
        else:
            if self.within_the_vision(map):
                dx, dy = map.actor.x - self.x, map.actor.y - self.y
                mag = pow(dx * dx + dy * dy, 0.5)
                if mag != 0:
                    dx, dy = dx / mag, dy / mag
                self.last_known_player_pos = (map.actor.x, map.actor.y)
            else:
                if self.last_known_player_pos:
                    dx, dy = self.last_known_player_pos[0] - self.x, self.last_known_player_pos[1] - self.y
                    mag = pow(dx * dx + dy * dy, 0.5)
                    if mag != 0:
                        dx, dy = dx / mag, dy / mag
                else:
                    x = random.randint(0, 4)
                    match x:
                        case 0:
                            dx, dy = 0, 1
                        case 1:
                            dx, dy = 0, -1
                        case 2:
                            dx, dy = 1, 0
                        case 3:
                            dx, dy = -1, 0
                        case _:
                            dx, dy = 0, 0  # Add this line

            if abs(dx) > abs(dy):
                self.move_mob(self.x + 1 if dx > 0 else self.x - 1, self.y, map)
            else:
                self.move_mob(self.x, self.y + 1 if dy > 0 else self.y - 1, map)
