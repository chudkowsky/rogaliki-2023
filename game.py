import curses
from enum import Enum
import fight as f
import actor as a
import item as i
import map as m
import map_parser as p
import mob_pack as pack


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
sword = i.Weapon(2, 2, rare, "miecz", 2)
armor = i.Armor(1, 2, common, "zbroja", 5)
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 80, 6)


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    map_window = curses.newwin(30, 40, 5, 5)  # Create a window for the map
    msg_window = curses.newwin(20, 60, 5, 45)  # Create a window for messages

    stdscr.addstr(3, 10, "Witaj w mojej grze, oto zasady:\n"
                            " - Poruszaj się strzałkami\n"
                            " - Aby wyświetlić informacje o mapie, naciśnij 'i'\n"
                            " - Aby przejść do gry, naciśnij dowolny klawisz\n"
                            " - Aby przejrzeć ekwipunek, naciśnij 'e'\n"
                            " - Aby przejrzeć plecak, naciśnij 'b'\n"
                            " - Aby podnieść przedmiot z mapy, naciśnij 'f'\n"
                            " - Aby założyć przedmiot z ekwipunku, naciśnij 'e', a następnie podaj numer przedmiotu\n")
    stdscr.refresh()

    mapka1 = m.Map(result[0], result[1], result[2], hero, [sword, armor], mobs)
    mapka1.set_mobs_and_items_on_map()
    stdscr.getch()
    stdscr.clear()
    while True:
        user_input = stdscr.getkey()
        map_window.clear()
        msg_window.clear()
        mapka1.show_stats(msg_window)
        moved = False
        if user_input == "KEY_UP":
            mapka1.move_person(mapka1.actor.x - 1, mapka1.actor.y)
            moved = True
        elif user_input == "KEY_DOWN":
            mapka1.move_person(mapka1.actor.x + 1, mapka1.actor.y)
            moved = True
        elif user_input == "KEY_LEFT":
            mapka1.move_person(mapka1.actor.x, mapka1.actor.y - 1)
            moved = True
        elif user_input == "KEY_RIGHT":
            mapka1.move_person(mapka1.actor.x, mapka1.actor.y + 1)
            moved = True
        elif user_input == "i":
            mapka1.show_info(msg_window)
        elif user_input == "b":
            hero.show_backpack(msg_window)
        elif user_input == "f":
            if (mapka1.check_if_item_to_collect()):
                mapka1.pick_item()
        elif user_input == "e":
            mapka1.actor.show_eq(msg_window)
            msg_window.addstr("Aby założyć przedmiot podaj jego numer!\n")
            msg_window.refresh()

            response = stdscr.getkey()
            if(response != '\x1b'):
                try:
                    item_number = int(response)
                    if 0 <= item_number < 6:
                        msg_window.addstr(f"Wybrałeś {mapka1.actor.backpack[item_number].name}. Wcisnij enter aby potwierdzić.")
                        msg_window.refresh()
                        confirm = stdscr.getkey()

                        if confirm == "\n":  # Check if Enter is pressed
                            mapka1.actor.add_to_eq(item_number)
                            msg_window.addstr(f"Przedmiot dodany do ekwipunku. ")
                        else:
                            msg_window.addstr(f"Anulowano dodawanie przedmiotu. ")
                    else:
                        msg_window.addstr("Niepoprawny numer przedmiotu. ")
                except ValueError:
                    msg_window.addstr("Niepoprawny format. Podaj numer przedmiotu. ")
            else:
                msg_window.refresh()
            msg_window.refresh()
        if moved and mapka1.check_if_item_to_collect():
            msg_window.addstr(f"Mozliwość podniesienia przedmiotu")
        if moved and f.within_attacking_distance(mapka1):
            msg_window.addstr(f"Przeciwnik w zasiegu!")
        mapka1.map_printer(map_window)
        msg_window.refresh()
        map_window.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
