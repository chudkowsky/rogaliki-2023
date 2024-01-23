from enum import Enum
import random

import item as i
import quality as q

rare = q.Quality.RARE
epic = q.Quality.EPIC
common = q.Quality.COMMON
legendary = q.Quality.LEGENDARY
class CommonItems():
    sword1 = i.Weapon(2, 2, common, "Żądło", 2)
    sword2 = i.Weapon(2, 2, common, "Anduril", 2)
    sword3 = i.Weapon(2, 2, common, "Glamdring", 2)
    sword4 = i.Weapon(2, 2, common, "Orcrist", 2)
    sword5 = i.Weapon(2, 2, common, "Narsil", 2)
    gloves1 = i.Gloves(2, 2, common, "Rękawice Mithrilu", 2)
    gloves2 = i.Gloves(2, 2, common, "Elfickie Naramienniki", 2)
    gloves3 = i.Gloves(2, 2, common, "Krasnoludzkie Rękawice Bojowe", 2)
    gloves4 = i.Gloves(2, 2, common, "Rękawice Strażnika", 2)
    gloves5 = i.Gloves(2, 2, common, "Rękawice Czarodzieja", 2)
    boots1 = i.Boots(2, 2, common, "Stópki Hobbita", 2)
    boots2 = i.Boots(2, 2, common, "Krasnoludzkie Buty Bojowe", 2)
    boots3 = i.Boots(2, 2, common, "Elfickie Buty", 2)
    boots4 = i.Boots(2, 2, common, "Buty Strażnika", 2)
    boots5 = i.Boots(2, 2, common, "Sandały Czarodzieja", 2)
    armor1 = i.Armor(1, 2, common, "Zbroja Mithrilu", 5)
    armor2 = i.Armor(1, 2, common, "Elfińska Kolczuga", 5)
    armor3 = i.Armor(1, 2, common, "Krasnoludzki Pancerz", 5)
    armor4 = i.Armor(1, 2, common, "Peleryna Strażnika", 5)
    armor5 = i.Armor(1, 2, common, "Szaty Czarodzieja", 5)
class RareItems():
    sword1 = i.Weapon(2, 2, rare, "Sierp Przeznaczenia", 2)
    sword2 = i.Weapon(2, 2, rare, "Mocna Długa Klinga", 2)
    sword3 = i.Weapon(2, 2, rare, "Wielka Klinga Niezłomności", 2)
    sword4 = i.Weapon(2, 2, rare, "Ostrze Wojennej Siły", 2)
    sword5 = i.Weapon(2, 2, rare, "Miecz Mistycznego Losu", 2)
    gloves1 = i.Gloves(2, 2, rare, "Rękawice Świetlistego Mithrilu", 2)
    gloves2 = i.Gloves(2, 2, rare, "Elfickie Rękawice Zwycięstwa", 2)
    gloves3 = i.Gloves(2, 2, rare, "Krasnoludzkie Rękawice Niezłomności", 2)
    gloves4 = i.Gloves(2, 2, rare, "Rękawice Mistrza Walki", 2)
    gloves5 = i.Gloves(2, 2, rare, "Rękawice Arkanicznej Mądrości", 2)
    boots1 = i.Boots(2, 2, rare, "Buty Złotych Śladów", 2)
    boots2 = i.Boots(2, 2, rare, "Krasnoludzkie Buty Bojowe Żywotności", 2)
    boots3 = i.Boots(2, 2, rare, "Elfickie Buty Skrytości", 2)
    boots4 = i.Boots(2, 2, rare, "Buty Strażnika Łotrzyka", 2)
    boots5 = i.Boots(2, 2, rare, "Sandały Magii Mroku", 2)
    armor1 = i.Armor(1, 2, rare, "Zbroja Świetlistego Mithrilu", 5)
    armor2 = i.Armor(1, 2, rare, "Elfińska Kolczuga Zwycięstwa", 5)
    armor3 = i.Armor(1, 2, rare, "Krasnoludzki Pancerz Niezłomności", 5)
    armor4 = i.Armor(1, 2, rare, "Peleryna Strażnika Mrocznej Nocy", 5)
    armor5 = i.Armor(1, 2, rare, "Szaty Czarodzieja Mistycznego Ognia", 5)


class EpicItems():
    sword1 = i.Weapon(2, 2, epic, "Krzyżówka Zapomnianego Mistrza", 2)
    sword2 = i.Weapon(2, 2, epic, "Długa Klinga Mrocznego Króla", 2)
    sword3 = i.Weapon(2, 2, epic, "Potężna Klinga Niezgody", 2)
    sword4 = i.Weapon(2, 2, epic, "Ostrze Wojennej Potęgi", 2)
    sword5 = i.Weapon(2, 2, epic, "Miecz Mistycznego Światła", 2)
    gloves1 = i.Gloves(2, 2, epic, "Rękawice Świetlistego Mistrza", 2)
    gloves2 = i.Gloves(2, 2, epic, "Elfickie Rękawice Zguby", 2)
    gloves3 = i.Gloves(2, 2, epic, "Krasnoludzkie Rękawice Nieśmiertelności", 2)
    gloves4 = i.Gloves(2, 2, epic, "Rękawice Króla Walki", 2)
    gloves5 = i.Gloves(2, 2, epic, "Rękawice Arcymaga Zniszczenia", 2)
    boots1 = i.Boots(2, 2, epic, "Buty Złotego Ducha", 2)
    boots2 = i.Boots(2, 2, epic, "Krasnoludzkie Buty Bojowe Żywiołów", 2)
    boots3 = i.Boots(2, 2, epic, "Elfickie Buty Skrytej Potęgi", 2)
    boots4 = i.Boots(2, 2, epic, "Buty Strażnika Przeznaczenia", 2)
    boots5 = i.Boots(2, 2, epic, "Sandały Magii Przekształcenia", 2)
    armor1 = i.Armor(1, 2, epic, "Zbroja Świetlistego Mithrilu", 5)
    armor2 = i.Armor(1, 2, epic, "Elfińska Kolczuga Zwycięstwa", 5)
    armor3 = i.Armor(1, 2, epic, "Krasnoludzki Pancerz Niezłomności", 5)
    armor4 = i.Armor(1, 2, epic, "Peleryna Strażnika Mrocznej Nocy", 5)
    armor5 = i.Armor(1, 2, epic, "Szaty Czarodzieja Mistycznego Ognia", 5)

class LegendaryItems():
    sword1 = i.Weapon(3, 3, legendary, "Miecz Legendarnego Bohatera", 3)
    sword2 = i.Weapon(3, 3, legendary, "Klinga Wiecznej Chwały", 3)
    sword3 = i.Weapon(3, 3, legendary, "Ognisty Miecz Smoka", 3)
    gloves1 = i.Gloves(3, 3, legendary, "Rękawice Nieśmiertelnej Mocy", 3)
    gloves2 = i.Gloves(3, 3, legendary, "Rękawice Mistrza Cienia", 3)
    boots1 = i.Boots(3, 3, legendary, "Buty Błyskawicznego Skradania", 3)
    boots2 = i.Boots(3, 3, legendary, "Buty Podróżnika Przestrzeni", 3)
    armor1 = i.Armor(2, 3, legendary, "Zbroja Niewzruszonego Obrońcy", 6)
    armor2 = i.Armor(2, 3, legendary, "Peleryna Zaklinacza Burz", 6)
    armor3 = i.Armor(2, 3, legendary, "Płomienna kolczuga Balrogów", 6)

def generate_random_items(item_class, num_items):
    items = []
    item_instances = [item for item in vars(item_class).values() if isinstance(item, i.Item)]

    if num_items > len(item_instances):
        raise ValueError("Number of requested items exceeds the available items in the class.")

    selected_items = random.sample(item_instances, num_items)

    for item_instance in selected_items:
        items.append(item_instance)
        item_instances.remove(item_instance)
    return items


def generate_combined_items(num_items,common_ratio,rare_ratio,epic_ratio,legendary_ratio):

    total_ratio = common_ratio + rare_ratio + epic_ratio+legendary_ratio

    common_items = generate_random_items(CommonItems, int(num_items * common_ratio / total_ratio))
    rare_items = generate_random_items(RareItems, int(num_items * rare_ratio / total_ratio))
    epic_items = generate_random_items(EpicItems, int(num_items * epic_ratio / total_ratio))
    legendary_items = generate_random_items(LegendaryItems, int(num_items * legendary_ratio / total_ratio))

    combined_items = common_items + rare_items + epic_items + legendary_items
    return combined_items


def items_for_each_lvl():
    result = []
    tmp = []
    c = 0.4
    r = 0.3
    e = 0.1
    l = 0.05
    for i in range(10):
        tmp = generate_combined_items(7,c,r,e,l)
        result.append(tmp.copy())
        c -= 0.05
        r += 0.12
        e += 0.13
        l += 0.1
        tmp.clear()
    return result
def test_print(result):
    i = 1
    for el in result:
        print(f"{i}:", end="")
        for item in el:
            print(item.name + ": " + str(item.quality.value[0]) + " ")
        print()
        i += 1

test_print(items_for_each_lvl())