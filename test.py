import copy
from enum import Enum
import mob_pack as pack
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


mob1 = pack.Mob.Hell_Dwarf.value
mob2 = pack.Mob.Rotten_Hobbit.value
mob3 = pack.Mob.Ork.value
mob4 = pack.Mob.Azog.value
mob5 = pack.Mob.Black_Spider.value
mobs = [mob1, mob2, mob3, mob4, mob5]
rare = Quality.RARE
epic = Quality.EPIC
common = Quality.COMMON
result = p.map_parser("map_parser_test")
sword = i.Weapon(2, 2, rare, "miecz",2 )
armor = i.Armor(1, 2, common, "zbroja",5 )
armor2 = i.Armor(1, 2, common, "zbroja",5 )
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 80, 6)
mapka1 = m.Map(result[0], result[1], result[2], hero, [sword, armor], mobs)
mapka1.set_mobs_and_items_on_map()


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


for mob in mobs:
    test_fight1(hero, mob, 10000, False)
print()
print()

test_fight1(hero, mob1, 1, True)

mapka1.map_printer()