import actor as a
import map_element as m
import item as i

wall = m.MapElement("wall", "#")
floor = m.MapElement("floor", "_")
it = i.Item()


class Map():

    def __init__(self, map_layout, x, y):
        self.map_layout = map_layout
        self.x = x
        self.y = y

    def map_printer(self):
        for j in range(self.y + 2):
            print("# ", end="")
        print()
        for i in range(self.x):
            print("# ", end="")
            for j in range(self.y):
                print(self.map_layout[i][j] + " ", end="")
            print('#')
        for j in range(self.y + 2):
            print("# ", end="")
        print('\n')

    def map_check(self):
        print("Na pozycji: ", self.x, ",", self.y, " znajduje się", self.map_layout[self.x][self.y])

    def map_delete(self, x, y):
        self.map_layout[x][y] = "#"

    def show_info(self):
        item_counter = 0
        person_counter = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.map_layout[i][j] == it.character:
                    item_counter += 1
                if self.map_layout[i][j] == a.Actor:
                    person_counter += 1
        print("Na mapie liczba przedmiotów to: ", item_counter, ", liczba postaci to: ", person_counter)

    def if_move_possible(self, x2, y2):
        if self.map_layout[x2][y2] == floor.character and x2 != self.x and y2 != self.y:
            return True
        else:
            return False

    def move_person(self, x1, y1, v):
        if v == "UP":
            if self.if_move_possible(x1 - 1, y1):
                self.map_layout[x1][y1] = floor.character
                self.map_layout[x1 - 1][y1] = "@"
                return True
        elif v == "DOWN":
            if self.if_move_possible(x1 + 1, y1):
                self.map_layout[x1][y1] = floor.character
                self.map_layout[x1 + 1][y1] = "@"
                return True
        elif v == "LEFT":
            if self.if_move_possible(x1, y1 - 1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1][y1 - 1] = "@"
                return True
        elif v == "RIGHT":
            if self.if_move_possible(x1, y1 + 1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1][y1 + 1] = "@"
                return True

    def map_swap(self, item, x, y):
        self.map_layout[x][y] = item.character
