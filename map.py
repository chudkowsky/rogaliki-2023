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
            self.map_layout[element.x][element.y].actor = element
        for element in self.items:
            self.map_layout[element.x][element.y].item = element

    def map_printer(self):
        flag = 0
        for i in range(self.x):
            for j in range(self.y):
                for element in self.mobs:
                    if element.x == i and element.y == j:
                        print(element.character + " ", end="")
                        flag = 1
                for element in self.items:
                    if element.x == i and element.y == j:
                        print(element.character + " ", end="")
                        flag = 1
                if self.actor.x == i and self.actor.y == j:
                    print(self.actor.character + " ", end="")
                    flag = 1
                if flag == 1:
                    flag = 0
                    continue
                else:
                    print(self.map_layout[i][j].character + " ", end="")
            print()

        self.show_info()

    def map_check(self, x, y):
        print("Na pozycji: ", x, ",", y, " znajduje się", self.map_layout[x][y].type)

    def map_check_mobs(self, x, y):
        for element in self.mobs:
            if element.x == x and element.y == y:
                return [True, element]
        return [False, None]

    def map_delete(self, x, y):
        self.map_layout[x][y] = m.Wall()

    def show_info(self):
        item_counter = len(self.items)
        person_counter = len(self.mobs) + 1
        print("Na mapie liczba przedmiotów to: ", item_counter, ", liczba postaci to: ", person_counter)

    def if_move_possible(self, x2, y2):
        for elements in self.mobs:
            if elements.x == x2 and elements.y == y2:
                return False
        for elements in self.items:
            if elements.x == x2 and elements.y == y2:
                return False
        if self.map_layout[x2][y2].placeable and x2 != self.x and y2 != self.y:
            return True
        else:
            return False

    def move_person(self, x1, y1, ):
        if self.if_move_possible(x1, y1):
            self.actor.x = x1
            self.actor.y = y1

    def map_swap(self, item, x, y):
        self.map_layout[x][y] = item
