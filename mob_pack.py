from enum import Enum
import actor as a


class Mob(Enum):
    Rotten_Hobbit = (a.Mob("medium", "Zgniły Hobbit", 3, 1, 8, 5, 8, 7, 100, 5))
    Hell_Dwarf = (a.Mob("small", "Piekielny karzeł", 8, 3, 3, 8, 4, 5, 80, 10))
    Ork = (a.Mob("big", "Ork", 2, 9, 10, 10, 3, 10, 115, 2))
    Black_Spider = (a.Mob("big", "Czarny Pajak", 3, 2, 9, 10, 10, 8, 80, 10))
    Azog = (a.Mob("big", "Azog Plugawy", 3, 5, 10, 10, 15, 10, 150, 10))

class Mob2(Enum):
    Goblin = a.Mob("small", "Goblin", 5, 5, 6, 7, 4, 6, 60, 8)
    Troll = a.Mob("big", "Troll", 1, 12, 12, 6, 2, 5, 200, 3)
    Dark_Wizard = a.Mob("medium", "Ciemny Czarodziej", 6, 8, 4, 9, 12, 10, 120, 7)
    Ice_Dragon = a.Mob("huge", "Lodowy Smok", 1, 15, 15, 8, 6, 12, 250, 5)
    Undead_Knight = a.Mob("medium", "Nieumarły Rycerz", 7, 7, 10, 5, 8, 9, 180, 6)
