import map as m
import actor as a
import item as i
import map_element as el


def test_map2():
    it = i.Item(2, 2)
    it2 = i.Item(1, 2)
    dog = a.Mob("medium", "dog", 3, 0)
    frog = a.Mob("small", "dog", 3, 3)
    hero = a.Person("Mateusz", 2, 1)
    mapatest = [[el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall()],
                [el.Wall(), el.Floor(), el.Wall(), el.Floor(), el.Wall()],
                [el.Wall(), el.Floor(), el.Wall(), el.Floor(), el.Wall()],
                [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Wall()]]
    mapka1 = m.Map(mapatest, 4, 5, hero, [it, it2], [dog, frog])
    mapka1.map_printer()
    print(mapka1.if_move_possible(1, 1))
    mapka1.show_info()
    mapka1.map_check(3, 3)
    mapka1.move_person(3, 1)
    mapka1.map_swap(el.Floor(), 0, 0)
    mapka1.map_printer()


test_map2()
