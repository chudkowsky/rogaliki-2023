import copy
from enum import Enum

import actor as a
import fight as f
import item as i
import map as m
import map_parser as p


class Quality(Enum):
    LEGENDARY = ("legendary", 4)
    EPIC = ("epic", 3)
    RARE = ("rare", 2)
    COMMON = ("common", 1)


rare = Quality.RARE
epic = Quality.EPIC

result = p.map_parser("map_parser_test")
sword = i.Weapon(2, 2, rare, 2,"miecz")
armor = i.Armor(1, 2, epic, 5,"zbroja")
dog = a.Mob("medium", "dog", 3, 1, 8, 5, 8, 7, 100, 5)
frog = a.Mob("small", "frog", 3, 3, 3, 3, 4, 5, 80, 10)
hero = a.Person("Mateusz", 3, 2, 9, 10, 10, 6, 80, 10)
hero2 = a.Person("Piotr", 3, 2, 9, 10, 10, 6, 80, 10)
mapka1 = m.Map(result[0], result[1], result[2], hero, [sword, armor], [dog, frog])
mapka1.set_mobs_and_items_on_map()
hero.add_to_eq(sword)
hero2.add_to_eq(armor)


def test_map1():
    mapka1.set_mobs_and_items_on_map()
    mapka1.map_printer()
    print(mapka1.map_layout[2][2].item.character)
    f.within_attacking_distance(mapka1)
    hero.attack(hero2, 0)


def test_fight1(hero1, dog1, n, flag):
    mob_wins = 0
    hero_wins = 0

    for it in range(n):
        hero_copy = copy.deepcopy(hero1)
        dog_copy = copy.deepcopy(dog1)

        if f.combat(hero_copy, dog_copy, flag):
            mob_wins += 1
        else:
            hero_wins += 1

    print(f"{dog1.name} won: {mob_wins} times and {hero1.name} won: {hero_wins} times")


test_fight1(hero, frog, 10000, False)
test_fight1(hero, hero2, 10000, False)
test_fight1(hero2, hero, 10000, False)
test_fight1(hero, dog, 10000, False)
test_fight1(hero2, frog, 10000, False)
test_fight1(hero2, dog, 10000, False)
print()
print()
test_fight1(hero2, hero, 1, True)
