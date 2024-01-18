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


mobs_list = [mob.value for mob in pack.Mob]

mobs2 = [mob.value for mob in pack.Mob2]
rare = Quality.RARE
epic = Quality.EPIC
common = Quality.COMMON
result = p.map_parser("map_parser_test")
result2 = p.map_parser("map_parser_test2")
sword = i.Weapon(2, 2, rare, "miecz", 2)
armor = i.Armor(1, 2, common, "zbroja", 5)
dagger = i.Weapon(1, 1, common, "sztylet", 3)
leather_armor = i.Armor(1, 1, common, "skórzana zbroja", 7)
great_sword = i.Weapon(4, 3, epic, "wielki miecz", 1)
plate_armor = i.Armor(2, 4, rare, "zbroja płytowa", 10)
magic_staff = i.Weapon(3, 1, epic, "magiczny kij", 4)
enchanted_robe = i.Armor(1, 1, epic , "zaklęta szata", 8)
items = [sword,armor,dagger,leather_armor,great_sword,plate_armor,magic_staff,enchanted_robe]
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 80, 6)


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    map_window = curses.newwin(36, 73, 3, 5)  # Create a window for the map
    msg_window = curses.newwin(30, 60, 6, 80)  # Create a window for messages

    stdscr.addstr(3, 10, "Witaj w mojej grze, oto zasady:\n"
                            " - Poruszaj się strzałkami\n"
                            " - Aby wyświetlić informacje o mapie, naciśnij 'i'\n"
                            " - Aby przejść do gry, naciśnij dowolny klawisz\n"
                            " - Aby przejrzeć ekwipunek, naciśnij 'e'\n"
                            " - Aby przejrzeć plecak, naciśnij 'b'\n"
                            " - Aby podnieść przedmiot z mapy, naciśnij 'f'\n"
                            " - Aby założyć przedmiot z ekwipunku, naciśnij 'e', a następnie podaj numer przedmiotu\n")
    stdscr.refresh()

    mapka1 = m.Map(result[0], result[1], result[2], hero, items, mobs_list)
    mapka1.set_mobs_and_items_on_map()
    stdscr.getch()
    stdscr.clear()
    mobs_killed = 0
    while True:
        user_input = stdscr.getkey()
        map_window.clear()
        msg_window.clear()
        mapka1.show_stats(msg_window,mobs_killed)
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
            mapka1.show_info(msg_window,1)
        elif user_input == "b":
            hero.show_backpack(msg_window)
        elif user_input == "f":
            if (mapka1.check_if_item_to_collect()):
                mapka1.pick_item()
        elif user_input == "e":
            #obsluga ekwipunku
            hero.equipment_display(msg_window,stdscr)
        elif user_input == "w" and f.within_attacking_distance(mapka1)[0]:
            #atakowanie
            if not (mapka1.actor.attack(f.within_attacking_distance(mapka1)[1],1,msg_window)):
                mobs_killed+=1
            msg_window.refresh()
        if moved and mapka1.check_if_item_to_collect():
            msg_window.addstr(f"Mozliwość podniesienia przedmiotu ")
        if moved and f.within_attacking_distance(mapka1)[0]:
            msg_window.addstr(f"Przeciwnik w zasiegu! ")
            msg_window.addstr(f"{f.within_attacking_distance(mapka1)[1].name} \n")
        if not mapka1.show_info(msg_window,0):
            #zamiana mapy na  nowa
            mapka1 = m.Map(result2[0], result2[1], result2[2], hero, items, mobs2)
            mapka1.set_mobs_and_items_on_map()
        mapka1.remove_dead_mobs()
        mapka1.map_printer(map_window)
        msg_window.refresh()
        map_window.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
