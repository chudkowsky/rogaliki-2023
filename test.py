import map as m
import actor as a
import item as i
import map_element as el
import map_parser as p
import fight as f
from enum import Enum
import copy


class Quality(Enum):
    LEGENDARY = ("legendary", 4)
    EPIC = ("epic", 3)
    RARE = ("rare", 2)
    COMMON = ("common", 1)


rare = Quality.RARE
epic = Quality.EPIC

result = p.map_parser("map_parser_test")
miecz = i.Weapon(2, 2, rare, 2)
it2 = i.Item(1, 2, epic)
dog = a.Mob("medium", "dog", 3, 1, 8, 10, 8, 7, 100, 5)
frog = a.Mob("small", "frog", 3, 3, 3, 3, 4, 5, 80, 10)
hero = a.Person("Mateusz", 3, 2, 9, 5, 8, 7, 85, 6)
hero2 = a.Person("Piotr", 3, 2, 6, 10, 10, 6, 80, 10)
mapka1 = m.Map(result[0], result[1], result[2], hero, [miecz, it2], [dog, frog])
mapka1.set_mobs_and_items_on_map()
hero.add_to_eq(miecz)
hero.apply_equipment_effects()


def test_map1():
    mapka1.set_mobs_and_items_on_map()
    mapka1.map_printer()
    print(mapka1.map_layout[2][2].item.character)
    f.within_attacking_distance(mapka1)
    hero.attack(hero2)


def test_fight1(hero1, dog1):
    mob_wins = 0
    hero_wins = 0

    for it in range(10000):
        hero_copy = copy.deepcopy(hero1)
        dog_copy = copy.deepcopy(dog1)

        if f.combat(hero_copy, dog_copy):
            mob_wins += 1
        else:
            hero_wins += 1

    print(f"{dog1.name} won: {mob_wins} times and {hero1.name} won: {hero_wins} times")


test_fight1(hero, frog)
test_fight1(hero, hero2)
test_fight1(hero, dog)
test_fight1(hero2, frog)
test_fight1(hero2, dog)