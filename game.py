import curses
import actor as a
import decorator
import item_pack
import map as m
import mob_pack as pack
import genarate_map as g
import quality as quality

mobs1 = [mob.value for mob in pack.SmallMob]
mobs2 = [mob.value for mob in pack.MediumMob]
mobs3 = [mob.value for mob in pack.BigMob]

rare = quality.Quality.RARE
epic = quality.Quality.EPIC
common = quality.Quality.COMMON
items = item_pack.items_for_each_lvl()
hero = a.Person("Roland", 3, 2, 9, 10, 10, 6, 800, 6)


def main(stdscr):
    maps = []
    lvl = 0
    for j in range(10):
        maps.append(g.make_rooms(35, 60, 20))
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()
    map_window = curses.newwin(36, 69, 3, 5)  # Create a window for the map
    msg_window = curses.newwin(30, 60, 6, 74)  # Create a window for messages

    decorator.decorate(stdscr)
    stdscr.refresh()

    mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items[lvl], [])
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
            mapka.actor.attack_with_key(mapka, mobs_killed, msg_window,"up")
            mapka.move_person(mapka.actor.x - 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_DOWN":
            mapka.actor.attack_with_key(mapka,mobs_killed,msg_window,"down")
            mapka.move_person(mapka.actor.x + 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_LEFT":
            mapka.actor.attack_with_key(mapka, mobs_killed, msg_window,"left")
            mapka.move_person(mapka.actor.x, mapka.actor.y - 1)
            moved = True
        elif user_input == "KEY_RIGHT":
            mapka.actor.attack_with_key(mapka, mobs_killed, msg_window,"right")
            mapka.move_person(mapka.actor.x, mapka.actor.y + 1)
            moved = True
        elif user_input == "\n":
            if (mapka.map_check(mapka.actor.x, mapka.actor.y) == "stairs" and not mapka.show_info(msg_window, 0)):
                lvl += 1
                mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items[lvl], [])
                mapka.adjust_mobs_to_lvl(lvl, mobs1.copy(), mobs2.copy(), mobs3.copy())
                mapka.set_mobs_and_items_on_map()
                msg_window.refresh()
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
        if moved and mapka.check_if_item_to_collect():
            msg_window.addstr(
                f"Mozliwość podniesienia przedmiotu: {mapka.map_check_item(mapka.actor.x, mapka.actor.y)[1].name}:"
                f"{mapka.map_check_item(mapka.actor.x, mapka.actor.y)[1].power}+")
        if moved and mapka.actor.within_attacking_distance(mapka)[0]:
            for elem in mapka.actor.within_attacking_distance(mapka)[1]:
                msg_window.addstr(f"Przeciwnik w zasiegu! ")
                msg_window.addstr(f"{elem[0].name} \n")
        msg_window.refresh()
        for mobs in mapka.mobs:
            if (mobs.alive):
                mobs.make_move(mob_attacked, mapka, msg_window)
            msg_window.refresh()
        msg_window.refresh()
        mapka.remove_dead_mobs()
        mapka.map_printer(map_window)
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
