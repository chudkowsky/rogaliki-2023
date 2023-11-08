
class item:
    name = '&'


class person:
    x = 0
    y = 0
    name = '@'


class map_element:
    wall = '#'
    floor = "_"

class Map():   
    
    def __init__(self,map_layout,x,y):
        self.map_layout = map_layout
        self.x = x
        self.y = y
    
    def map_printer(self):
        for j in range (self.y+1):
            print(" _",end="")
        print('\n')   
        for i in range(self.x):
            print("| ",end="")
            for j in range(self.y):
                print (self.map_layout[i][j]+" ", end="")  
            print('|')
        for j in range (self.y+1):
            print(" _",end="")
        print('\n')
        
    def map_check(self):
        print("Na pozycji: ",self.x,",",self.y," znajduje się", self.map_layout[self.x][self.y])
    
    def map_swap(self):
        self.map_layout[self.x][self.y] = item.name
        
    def show_info(self):
        item_counter = 0
        person_counter = 0
        for i in range(self.x):
            for j in range(self.y):
                if(self.map_layout[i][j]==item.name):
                    item_counter+=1
                if(self.map_layout[i][j]==person.name):
                    person_counter+=1
        print("Na mapie liczba przedmiotów to: ",item_counter,", liczba postaci to: ",person_counter)

    def if_move_possible(self,x2,y2):
        if(self.map_layout[x2][y2] == map_element.floor and x2!=self.x and y2!=self.y):
            return True
        else:
            return False
        
    def move_person(self, x1, y1, v):
        if v == "UP":
            if self.if_move_possible(x1 - 1, y1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1 - 1][y1] = "@"
        elif v == "DOWN":
            if self.if_move_possible(x1 + 1, y1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1 + 1][y1] = "@"
        elif v == "LEFT":
            if self.if_move_possible(x1, y1 - 1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1][y1 - 1] = "@"
        elif v == "RIGHT":
            if self.if_move_possible(x1, y1 + 1):
                self.map_layout[x1][y1] = "_"
                self.map_layout[x1][y1 + 1] = "@"
    
    
    
    def map_swap(self,item,x,y):
        self.map_layout[x][y] = item.name


    
def test_map():
    mapa1 = [['#', '#', '#', '#', '#'],
            ['#', '_', '_', '#', '#'],
            ['#', '@', '_', '&', '#'],
            ['#', '#', '&', '#', '#']
            ]
    
    mapa2 = [['#', '#', '#', '#', '#'],
            ['#', '@', '#', '#', '#'],
            ['&', '#', '#', '&', '#'],
            ['#', '#', '&', '#', '#']]
    
    mapa3 = [['&', '#', '#', '#', '#'],
            ['#', '@', '#', '#', '#'],
            ['#', '#', '#', '&', '#'],
            ['#', '#', '#', '#', '#']]
    
    mapa4 = [['#', '#', '#', '#', '#'],
            ['#', '#', '#', '#', '#'],
            ['#', '#', '#', '&', '#'],
            ['#', '@', '#', '#', '#']]
    mapka = Map(mapa1, 4, 5)
    #mapka.map_printer()
    mapka.move_person(2,1,"UP")
    #mapka.map_printer()


test_map()
