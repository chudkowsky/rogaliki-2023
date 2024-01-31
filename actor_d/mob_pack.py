from enum import Enum
from actor_d import actor as a


class SmallMob(Enum):
    Rotten_Hobbit = a.Mob("small", "Zgniły leśnik", 3, 1, 3, 5, 8, 7, 40, 5)
    Hell_Dwarf = a.Mob("small", "Piekielny karzeł", 8, 3, 3, 8, 4, 5, 40, 10)
    Ork = a.Mob("small", "Cabrioletton", 2, 9, 4, 10, 3, 10, 30, 2)
    Black_Spider = a.Mob("small", "Czarny Pająk", 3, 2, 4, 7, 7, 8, 50, 5)
    Azog = a.Mob("small", "Jaskiniowy Goblin", 3, 5, 5, 5, 6, 10, 60, 5)


class MediumMob(Enum):
    Goblin = a.Mob("medium", "Goblin", 5, 5, 6, 7, 4, 6, 60, 8)
    Troll = a.Mob("medium", "Troll", 1, 12, 12, 3, 2, 5, 200, 1)
    Dark_Wizard = a.Mob("medium", "Ciemny Czarodziej", 6, 8, 4, 9, 12, 10, 120, 7)
    Ice_Dragon = a.Mob("medium", "Lodowy Smok", 1, 15, 15, 8, 6, 12, 250, 5)
    Undead_Knight = a.Mob("medium", "Nieumarły Rycerz", 7, 7, 10, 5, 8, 9, 180, 6)


class BigMob(Enum):
    Huge_Orc = a.Mob("big", "Wielki Ork", 4, 10, 8, 8, 4, 7, 150, 8)
    Fire_Giant = a.Mob("big", "Upadły Książe Targon", 3, 18, 18, 7, 3, 8, 300, 4)
    Hydra = a.Mob("big", "Hydra", 2, 20, 20, 10, 5, 15, 400, 6)
    Demon_Lord = a.Mob("big", "Władca Demonów", 5, 25, 25, 12, 8, 20, 500, 10)
    Ancient_Dragon = a.Mob("big", "Starożytny Smok", 2, 30, 30, 15, 10, 25, 600, 12)
