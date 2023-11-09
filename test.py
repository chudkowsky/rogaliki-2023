import map as m
import actor as a
import game as g
import item as i
import map_element as el

'''
def test_map():

    mapa1 = [['#', '#', '#', '#', '#'],
             ['#', '_', '#', ' ', '#'],
             ['#', '@', '#', '&', '#'],
             ['#', ' ', '&', ' ', '#']
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
    mapka1 = m.Map(mapa1, 4, 5)
    mapka2 = m.Map(mapa2, 4, 5)
    mapka3 = m.Map(mapa3, 4, 5)
    mapka4 = m.Map(mapa4, 4, 5)
    mapka1.map_printer()
    mapka1.move_person(2, 1, "UP")
    mapka1.map_printer()
    print(False == mapka2.if_move_possible(0, 0))
    sword = i.Item()
    print("Mapa przed zmiana: ")
    mapka2.map_printer()
    mapka2.map_swap(sword, 0, 0)
    print("Mapa po zmianie: ")
    mapka2.map_printer()

    print("Mapa przed zmiana: ")
    mapka3.map_printer()
    mapka3.map_delete(0, 0)
    print("Mapa po zmianie: ")
    mapka3.map_printer()
    mapka4.show_info()
'''


# test_map()

def test_map2():
    wall = el.Wall("wall", "#")
    floor = el.Floor("floor", "_")
    it = i.Item(2, 2)
    it2 = i.Item(1, 2)
    dog = a.Mob("medium","dog",4,0)
    frog = a.Mob("small","dog",3,3)
    hero = a.Person("Mateusz", 2, 1)
    mapatest = [[wall, wall, wall, wall, wall],
                [wall, floor, wall, floor, wall],
                [wall, floor, wall, it, wall],
                [wall, floor, it, floor, wall]]
    mapka1 = m.Map(mapatest, 4, 5, hero, [it, it2], [dog,frog])
    mapka1.map_printer()
    print(mapka1.if_move_possible(1,1))
    mapka1.show_info()


test_map2()
