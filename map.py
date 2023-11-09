import actor as a
import map_element as m


class Map():

    def __init__(self, map_layout, x, y, actor: a.Person, items: list, mobs: list):
        self.map_layout = map_layout
        self.x = x
        self.y = y
        self.actor = actor
        self.items = items
        self.mobs = mobs

    def map_printer(self):
        for j in range(self.y + 2):
            print("# ", end="")
        print()
        for i in range(self.x):
            print("# ", end="")
            for j in range(self.y):
                print(self.map_layout[i][j].character + " ", end="")
            print('#')
        for j in range(self.y + 2):
            print("# ", end="")
        print('\n')

    def map_check(self, x, y):
        print("Na pozycji: ", x, ",", y, " znajduje się", self.map_layout[x][y].type)

    def map_delete(self, x, y):
        self.map_layout[x][y] = m.Wall("wall", "#")

    def show_info(self):
        item_counter = len(self.items)
        person_counter = len(self.mobs) + 1
        print("Na mapie liczba przedmiotów to: ", item_counter, ", liczba postaci to: ", person_counter)

    def if_move_possible(self, x2, y2):
        for elements in self.mobs:
            if(elements.x == x2 and elements.y == y2):
                return False
        for elements in self.items:
            if(elements.x == x2 and elements.y == y2):
                return False
        if isinstance(self.map_layout[x2][y2], m.Floor) and x2 != self.x and y2 != self.y:
            return True
        else:
            return False

    def move_person(self, x1, y1, v):
        if v == "UP":
            if self.if_move_possible(x1 - 1, y1):
                self.map_layout[x1][y1] = m.Floor("floor", "_")
                self.map_layout[x1 - 1][y1] = self.actor
                return True
        elif v == "DOWN":
            if self.if_move_possible(x1 + 1, y1):
                self.map_layout[x1][y1] = m.Floor("floor", "_")
                self.map_layout[x1 + 1][y1] = self.actor
                return True
        elif v == "LEFT":
            if self.if_move_possible(x1, y1 - 1):
                self.map_layout[x1][y1] = m.Floor("floor", "_")
                self.map_layout[x1][y1 - 1] = self.actor
                return True
        elif v == "RIGHT":
            if self.if_move_possible(x1, y1 + 1):
                self.map_layout[x1][y1] = m.Floor("floor", "_")
                self.map_layout[x1][y1 + 1] = self.actor
                return True

    def map_swap(self, item, x, y):
        self.map_layout[x][y] = item
