import curses
import random

import actor as a
import map_element as m


class Map:

    def __init__(self, map_layout, x, y, actor: a.Person, items, mobs):
        self.map_layout = map_layout
        self.x = x
        self.y = y
        self.actor = actor
        self.items = items
        self.mobs = mobs

    def set_mobs_and_items_on_map(self):
        for element in self.mobs:
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            while(not self.if_move_possible(x,y)):
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

    def map_printer(self, stdscr):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        for i in range(self.x):
            for j in range(self.y):
                if self.actor.x == i and self.actor.y == j:
                    stdscr.addch(i, j, self.actor.character)
                elif any(element.x == i and element.y == j for element in self.mobs):
                    mob = next(element for element in self.mobs if element.x == i and element.y == j)
                    stdscr.addch(i, j, mob.character, curses.color_pair(1))
                elif any(element.x == i and element.y == j for element in self.items):
                    item = next(element for element in self.items if element.x == i and element.y == j)
                    stdscr.addch(i, j, item.character, curses.color_pair(3))
                else:
                    if self.map_layout[i][j].placeable:
                        stdscr.addch(i, j, self.map_layout[i][j].character, curses.color_pair(1))
                    else:
                        stdscr.addch(i, j, self.map_layout[i][j].character, curses.color_pair(2))

    def map_check(self, x, y):
        return self.map_layout[x][y].type

    def map_check_mobs(self, x, y):
        for element in self.mobs:
            if element.x == x and element.y == y:
                return [True, element]
        return [False, None]

    def map_delete(self, x, y):
        self.map_layout[x][y] = m.Wall()

    def show_info(self, stdscr, flag):
        item_counter = len(self.items)
        person_counter = len(self.mobs) + 1
        if flag:
            stdscr.addstr(f"Na mapie liczba przedmiotów to: {item_counter}, liczba postaci to: {person_counter}")
        return person_counter - 1

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

    def map_swap(self, item, x, y):
        self.map_layout[x][y] = item

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

    def show_stats(self, stdscr, counter):
        stdscr.addstr(f"{self.actor.name}\n"
                      f"HP:{self.actor.health} "
                      f"STRENGTH:{self.actor.strength} "
                      f"DEFENCE:{self.actor.defence}\n"
                      f"MOBS KILLED:{counter}\n")

    def remove_dead_mobs(self):
        index = 0
        for mob in self.mobs:
            if not mob.alive:
                self.mobs.pop(index)
            index += 1
