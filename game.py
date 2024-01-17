import curses

import actor
import fight
import map_parser as p
import copy
from enum import Enum
import mob_pack as pack
import actor as a
import fight as f
import item as i
import map as m

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
armor = i.Armor(1, 2, common, "zbroja",5)
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 80, 6)



def main(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, f"Witaj w mojej grze, o to zasady:\n -poruszasz sie strzałkami\n "
                        f"-aby wyswietlic informacje o mapie nacisnij i \n "
                        f"-aby przejść do gry nacisnij jakikolwiek klawisz\n "
                        f"-aby przejrzeć ekwipunek nacisnij klawisz e\n"
                        f"-aby przejrzec plecak nacisnij b\n")
    stdscr.refresh()
    mapka1 = m.Map(result[0], result[1], result[2], hero, [sword, armor], mobs)
    mapka1.set_mobs_and_items_on_map()

    while True:

        user_input = stdscr.getkey()
        stdscr.clear()
        moved = False
        if user_input == "KEY_UP":
            mapka1.move_person(mapka1.actor.x-1, mapka1.actor.y)
            moved = True
        elif user_input == "KEY_DOWN":
            mapka1.move_person(mapka1.actor.x+1, mapka1.actor.y)
            moved = True
        elif user_input == "KEY_LEFT":
            mapka1.move_person(mapka1.actor.x, mapka1.actor.y-1)
            moved = True
        elif user_input == "KEY_RIGHT":
            mapka1.move_person(mapka1.actor.x, mapka1.actor.y+1)
            moved = True
        elif user_input == "i":
            mapka1.show_info(stdscr)
        elif user_input == "b":
            hero.show_backpack(stdscr)
        elif user_input == "f":
            if(mapka1.check_if_item_to_collect()):
                mapka1.pick_item()
        if (moved == True):
            if(mapka1.check_if_item_to_collect()):
                stdscr.addstr(15, 25, f" Mozliwość podniesienia przedmiotu")

        mapka1.map_printer(stdscr)
        stdscr.addstr(15, 15, f"{user_input}")
        stdscr.refresh()
        # Print user input at the bottom of the screen

        # Wait for user input


# Run the curses application
if __name__ == "__main__":
    curses.wrapper(main)


