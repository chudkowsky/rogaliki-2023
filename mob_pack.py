from enum import Enum
import actor as a


class Mob(Enum):
    Rotten_Hobbit = (a.Mob("medium", "Zgniły Hobbit", 3, 1, 8, 5, 8, 7, 100, 5))
    Hell_Dwarf = (a.Mob("small", "Piekielny karzeł", 3, 3, 3, 8, 4, 5, 80, 10))
    Ork = (a.Mob("big", "Ork", 2, 9, 10, 10, 3, 10, 115, 2))
    Black_Spider = (a.Mob("big", "Czarny Pajak", 3, 2, 9, 10, 10, 8, 80, 10))
    Azog = (a.Mob("big", "Azog Plugawy", 3, 2, 10, 10, 15, 10, 150, 10))
