class item:
    name = '&'


class person:
    x = 0
    y = 0
    name = '@'


class map_element:
    wall = '#'
    floor = "_"


def map_manager(mapa,n, m):
    show_info(mapa, n, m)


def move_person(mapa,n,m,x1,y1,v):
    if(v == "UP"):
        if(if_move_possible(mapa, n, m, x1-1, y1)):
            mapa[x1][y1] = "_"
            mapa[x1-1][y1] = "@"
            
    if(v == "DOWN"):
        if(if_move_possible(mapa, n, m, x1+1, y1)):
            mapa[x1][y1] = "_"
            mapa[x1+1][y1] = "@"
    if(v == "LEFT"):
        if(if_move_possible(mapa, n, m, x1, y1-1)):
            mapa[x1][y1] = "_"
            mapa[x1][y1-1] = "@"
    if(v == "RIGHT"):
        if(if_move_possible(mapa, n, m, x1, y1+1)):
            mapa[x1][y1] = "_"
            mapa[x1][y1+1] = "@"
    
def if_move_possible(mapa,n,m,x2,y2):
    if(mapa[x2][y2] == map_element.floor and x2!=n and y2!=m):
        return True
    else:
        return False
    
def show_info(mapa,n,m):
    item_counter = 0
    person_counter = 0
    for i in range(n):
        for j in range(m):
            if(mapa[i][j]==item.name):
                item_counter+=1
            if(mapa[i][j]==person.name):
                person_counter+=1
    print("Na mapie liczba przedmiotów to: ",item_counter,", liczba postaci to: ",person_counter)
    

def map_printer(mapa,n,m):
    for j in range (m+1):
        print(" _",end="")
    print('\n')   
    for i in range(n):
        print("| ",end="")
        for j in range(m):
            print (mapa[i][j]+" ", end="")  
        print('|')
    for j in range (m+1):
        print(" _",end="")
    print('\n')
    

def map_swap(mapa,item,x,y):
    mapa[x][y] = item.name

def map_check(mapa,x,y):
    print("Na pozycji: ",x,",",y," znajduje się", mapa[x][y])
    
def test_map():
    mapa1 = [['#', '#', '#', '#', '#'],
            ['#', '_', '_', '#', '#'],
            ['#', '@', '_', '&', '#'],
            ['#', '#', '&', '#', '#']]
    
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

    map_printer(mapa1,4,5)
    move_person(mapa1,4,5,2,1,"UP")
    map_printer(mapa1,4,5)

test_map()