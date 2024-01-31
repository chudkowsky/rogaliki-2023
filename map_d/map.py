import curses
import random
from actor_d import actor as a
from map_d import map_element as m


class Map:

    def __init__(self, map_layout, x, y, actor: a.Person, items, mobs):
        self.map_layout = map_layout
        self.x = x
        self.y = y
        self.actor = actor
        self.items = items
        self.mobs = mobs

    def set_mobs_and_items_on_map(self):
        for i in range(int(len(self.items) / 2)):
            if (self.items[i].type == 'potion'):
                self.mobs[i].equipment.append(self.items.pop(i))
                self.mobs[i].equipment[0].apply_item_effect(self.mobs[i])
        for element in self.mobs:
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            while not self.if_move_possible(x, y):
                x = random.randint(0, self.x - 1)
                y = random.randint(0, self.y - 1)
            element.x = x
            element.y = y
            self.map_layout[element.x][element.y].actor = element
        for element in self.items:
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            while (not self.if_move_possible(x, y)):
                x = random.randint(0, self.x - 1)
                y = random.randint(0, self.y - 1)
            element.x = x
            element.y = y
            self.map_layout[element.x][element.y].item = element
        x = random.randint(0, self.x - 1)
        y = random.randint(0, self.y - 1)
        while (not self.if_move_possible(x, y)):
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
        self.actor.x = x
        self.actor.y = y

    def map_printer(self, stdscr):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
        for i in range(self.x):
            for j in range(self.y):
                if self.actor.x == i and self.actor.y == j:
                    stdscr.addch(i, j, self.actor.character)
                elif any(element.x == i and element.y == j for element in self.mobs):
                    mob = next(element for element in self.mobs if element.x == i and element.y == j)
                    stdscr.addch(i, j, mob.character, curses.color_pair(1))
                elif any(element.x == i and element.y == j for element in self.items):
                    item = next(element for element in self.items if element.x == i and element.y == j)
                    if item.quality.value[1] == 3:
                        stdscr.addch(i, j, item.character, curses.color_pair(4))
                    elif item.quality.value[1] == 2:
                        stdscr.addch(i, j, item.character, curses.color_pair(5))
                    else:
                        stdscr.addch(i, j, item.character, curses.color_pair(3))
                else:
                    if self.map_layout[i][j].placeable:
                        stdscr.addch(i, j, self.map_layout[i][j].character, curses.color_pair(1))
                    else:
                        stdscr.addch(i, j, self.map_layout[i][j].character, curses.color_pair(2))

    def map_printer2(self, stdscr):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)

        start_x = max(self.actor.x - 5, 0)
        end_x = min(self.actor.x + 6, self.x)
        start_y = max(self.actor.y - 20, 0)
        end_y = min(self.actor.y + 21, self.y)

        center_x = 5
        center_y = 10

        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                screen_x = i - start_x + center_x
                screen_y = j - start_y + center_y
                if (i == end_y - 1):
                    stdscr.addch(screen_x, screen_y, "#", curses.color_pair(3))
                if self.actor.x == i and self.actor.y == j:
                    stdscr.addch(screen_x, screen_y, self.actor.character)
                elif any(element.x == i and element.y == j for element in self.mobs):
                    mob = next(element for element in self.mobs if element.x == i and element.y == j)
                    stdscr.addch(screen_x, screen_y, mob.character, curses.color_pair(1))
                elif any(element.x == i and element.y == j for element in self.items):
                    item = next(element for element in self.items if element.x == i and element.y == j)
                    if item.quality.value[1] == 3:
                        stdscr.addch(screen_x, screen_y, item.character, curses.color_pair(4))
                    elif item.quality.value[1] == 2:
                        stdscr.addch(screen_x, screen_y, item.character, curses.color_pair(5))
                    else:
                        stdscr.addch(screen_x, screen_y, item.character, curses.color_pair(3))
                else:
                    if self.map_layout[i][j].placeable:
                        stdscr.addch(screen_x, screen_y, self.map_layout[i][j].character, curses.color_pair(1))
                    else:
                        stdscr.addch(screen_x, screen_y, self.map_layout[i][j].character, curses.color_pair(2))

    def map_check(self, x, y):
        return self.map_layout[x][y].type

    def adjust_mobs_to_lvl(self, lvl, mobs1, mobs2, mobs3):
        if 0 <= lvl < 3:
            for elem in mobs1:
                elem.alive = True
            self.mobs = mobs1
        elif 3 <= lvl < 6:
            for elem in mobs2:
                elem.alive = True
            self.mobs = mobs2
        else:
            for elem in mobs3:
                elem.alive = True
            self.mobs = mobs3

    def map_check_mobs(self, x, y):
        for element in self.mobs:
            if element.x == x and element.y == y:
                return [True, element]
        return [False, None]

    def map_check_item(self, x, y):
        for element in self.items:
            if element.x == x and element.y == y:
                return [True, element]
        return [False, None]

    def map_delete(self, x, y):
        self.map_layout[x][y] = m.Wall()

    def show_info(self, stdscr, flag):
        item_counter = len(self.items)
        person_counter = len(self.mobs)
        if flag:
            stdscr.addstr(f"Na mapie liczba przedmiotów to: {item_counter}, liczba potworów to: {person_counter}")
        return person_counter

    def if_move_possible(self, x2, y2):
        for elements in self.mobs:
            if elements.x == x2 and elements.y == y2:
                return False
        if self.map_layout[x2][y2].placeable and x2 != self.x and y2 != self.y:
            return True
        else:
            return False

    def move_person(self, x1, y1):
        print(f"Moving actor to ({x1}, {y1})")
        if self.if_move_possible(x1, y1):
            self.actor.x = x1
            self.actor.y = y1
        else:
            print("move not possible")

    def map_swap(self, item):
        self.items.append(item)

    def check_if_item_to_collect(self):
        for elem in self.items:
            if self.actor.x == elem.x:
                if self.actor.y == elem.y:
                    return True
                else:
                    return False

    def pick_item(self):
        items_copy = self.items.copy()
        for item in items_copy:
            if self.actor.x == item.x and self.actor.y == item.y:
                self.items.remove(item)
                self.actor.add_to_backpack(item)

    def show_stats(self, stdscr, counter, lvl):

        black = "."
        white = "#"
        progress = ""
        for i in range(5):
            if not i < counter:
                progress += black
            else:
                progress += white

        stdscr.addstr(0, 0, f"{self.actor.name}\n"
                            f"HP:{self.actor.health} "
                            f"Siła:{self.actor.strength} "
                            f"Defensywa:{self.actor.defence}\n"
                            f"Walka wręcz: {self.actor.hand_to_hand_combat} "
                            f"Zwinność: {self.actor.agility} \n"
                            f"Pokonani przeciwnicy:{counter}\n"
                            f"{progress} "
                            f"LVL:{lvl + 1}\n"
                            f"--------------------------------\n")
        stdscr.refresh()  # Refresh the screen to display the changes

    def remove_dead_mobs(self):
        index = 0
        for mob in self.mobs:
            if not mob.alive:
                self.mobs.pop(index)
            index += 1
