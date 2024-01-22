import curses
from enum import Enum
import actor as a
import item as i
import map as m
import map_parser as p
import mob_pack as pack
import genarate_map as g


class Quality(Enum):
    LEGENDARY = ("legendary", 4)
    EPIC = ("epic", 3)
    RARE = ("rare", 2)
    COMMON = ("common", 1)


mobs1 = [mob.value for mob in pack.SmallMob]
mobs2 = [mob.value for mob in pack.MediumMob]
mobs3 = [mob.value for mob in pack.BigMob]
rare = Quality.RARE
epic = Quality.EPIC
common = Quality.COMMON

result2 = p.map_parser("map_parser_test2")
sword = i.Weapon(2, 2, rare, "miecz", 2)
armor = i.Armor(1, 2, common, "zbroja", 5)
dagger = i.Weapon(1, 1, common, "sztylet", 3)
leather_armor = i.Armor(1, 1, common, "skórzana zbroja", 7)
great_sword = i.Weapon(4, 3, epic, "wielki miecz", 1)
plate_armor = i.Armor(2, 4, rare, "zbroja płytowa", 10)
magic_staff = i.Weapon(3, 1, epic, "magiczny kij", 4)
enchanted_robe = i.Armor(1, 1, epic, "zaklęta szata", 8)
healing_potion = i.HealingPotion(1, 1, epic, "Leczący wywar z ziemniaków i żyta", 5)
items = [sword, armor, dagger, leather_armor, great_sword, plate_armor, magic_staff, enchanted_robe, healing_potion]
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 800, 6)


def main(stdscr):
    maps = []
    lvl = 0
    for j in range(11):
        maps.append(g.make_rooms(35, 50, 20))
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()
    map_window = curses.newwin(36, 69, 3, 5)  # Create a window for the map
    msg_window = curses.newwin(30, 60, 6, 74)  # Create a window for messages

    stdscr.addstr(3, 10, "Witaj w mojej grze, oto zasady:\n"
                         " - Poruszaj się strzałkami\n"
                         " - Aby wyświetlić informacje o mapie, naciśnij 'i'\n"
                         " - Aby przejść do gry, naciśnij dowolny klawisz\n"
                         " - Aby przejrzeć ekwipunek, naciśnij 'e'\n"
                         " - Aby przejrzeć plecak, naciśnij 'b'\n"
                         " - Aby podnieść przedmiot z mapy, naciśnij 'f'\n"
                         " - Aby założyć przedmiot z ekwipunku, naciśnij 'e', a następnie podaj numer przedmiotu\n")
    stdscr.refresh()

    mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items, [])
    mapka.adjust_mobs_to_lvl(lvl, mobs1.copy(), mobs2.copy(), mobs3.copy())
    mapka.set_mobs_and_items_on_map()

    stdscr.getch()
    stdscr.clear()
    mobs_killed = 0
    mob_attacked = True
    while True:
        user_input = stdscr.getkey()
        map_window.clear()
        msg_window.clear()
        mapka.show_stats(msg_window, mobs_killed, lvl)
        moved = False
        if user_input == "KEY_UP":
            mapka.move_person(mapka.actor.x - 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_DOWN":
            mapka.move_person(mapka.actor.x + 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_LEFT":
            mapka.move_person(mapka.actor.x, mapka.actor.y - 1)
            moved = True
        elif user_input == "KEY_RIGHT":
            mapka.move_person(mapka.actor.x, mapka.actor.y + 1)
            moved = True
        elif user_input == "i":
            mapka.show_info(msg_window, 1)
        elif user_input == "b":
            hero.show_backpack(msg_window)
        elif user_input == "f":
            if (mapka.check_if_item_to_collect()):
                mapka.pick_item()
        elif user_input == "e":
            # obsluga ekwipunku
            hero.equipment_display(msg_window, stdscr)
        elif user_input == "w" and mapka.actor.within_attacking_distance(mapka)[0]:
            # atakowanie
            if not (mapka.actor.attack(mapka.actor.within_attacking_distance(mapka)[1], 1, msg_window)):
                mobs_killed += 1
                mob_attacked = True
            msg_window.refresh()
        if moved and mapka.check_if_item_to_collect():
            msg_window.addstr(
                f"Mozliwość podniesienia przedmiotu: {mapka.map_check_item(mapka.actor.x, mapka.actor.y)[1].name}")
        if moved and mapka.actor.within_attacking_distance(mapka)[0]:
            msg_window.addstr(f"Przeciwnik w zasiegu! ")
            msg_window.addstr(f"{mapka.actor.within_attacking_distance(mapka)[1].name} \n")
        if not mapka.show_info(msg_window, 0):
            lvl += 1
            # zamiana mapy na  nowa
            mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items, [])
            mapka.adjust_mobs_to_lvl(lvl, mobs1, mobs2, mobs3)
            mapka.set_mobs_and_items_on_map()
        msg_window.refresh()

        for mobs in mapka.mobs:
            if (mobs.alive):
                mobs.make_move(mob_attacked, mapka, msg_window)
            msg_window.refresh()
        msg_window.refresh()
        mapka.remove_dead_mobs()
        mapka.map_printer2(map_window)
        msg_window.refresh()
        map_window.refresh()
        if not hero.alive:
            break
    stdscr.clear()
    stdscr.addstr("Umarłeś!")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
