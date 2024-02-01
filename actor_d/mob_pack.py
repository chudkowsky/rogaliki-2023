from enum import Enum
from actor_d import actor as a

class SmallMob(Enum):
    Gollum = a.Mob("small", "Gollum", 3, 1, 3, 5, 8, 7, 40, 5)
    Gimli = a.Mob("small", "Gimli", 8, 3, 3, 8, 4, 5, 40, 10)
    Orc = a.Mob("small", "Orc", 2, 9, 4, 10, 3, 10, 30, 2)
    Shelob = a.Mob("small", "Shelob", 3, 2, 4, 7, 7, 8, 50, 5)
    Azog = a.Mob("small", "Azog", 3, 5, 5, 5, 6, 10, 60, 5)

class MediumMob(Enum):
    Legolas = a.Mob("medium", "Legolas", 5, 5, 6, 7, 4, 6, 60, 8)
    Cave_Troll = a.Mob("medium", "Cave Troll", 1, 12, 12, 3, 2, 5, 200, 1)
    Saruman = a.Mob("medium", "Saruman", 6, 8, 4, 9, 12, 10, 120, 7)
    Smaug = a.Mob("medium", "Smaug", 1, 15, 15, 8, 6, 12, 250, 5)
    Nazgul = a.Mob("medium", "Nazgul", 7, 7, 10, 5, 8, 9, 180, 6)

class BigMob(Enum):
    Uruk_hai = a.Mob("big", "Uruk-hai", 4, 10, 8, 8, 4, 7, 150, 8)
    Balrog = a.Mob("big", "Balrog", 3, 18, 18, 7, 3, 8, 300, 4)
    Watcher_in_the_Water = a.Mob("big", "Watcher in the Water", 2, 20, 20, 10, 5, 15, 400, 6)
    Sauron = a.Mob("big", "Sauron", 5, 25, 25, 12, 8, 20, 500, 10)
    Ancalagon = a.Mob("big", "Ancalagon the Black", 2, 30, 30, 15, 10, 25, 600, 12)
