import curses
from actor_d import actor as a
from actor_d import player_choosing as p
from interface import decorator
from item_d import item_pack as item_pack
from map_d import map as m, genarate_map as g
from actor_d import mob_pack as pack

mobs1 = [mob.value for mob in pack.SmallMob]
mobs2 = [mob.value for mob in pack.MediumMob]
mobs3 = [mob.value for mob in pack.BigMob]

items = item_pack.items_for_each_lvl()
hero1 = a.Person("Zwinny Elf", 3, 2, 8, 5, 10, 8, 150, 14)
hero2 = a.Person("Mocarny Krasnolud", 3, 2, 12, 10, 5, 6, 300, 6)
hero3 = a.Person("Bard z Jezior", 3, 2, 9, 10, 8, 7, 200, 8)


def main(stdscr):
    maps = []
    lvl = 0
    for j in range(10):
        maps.append(g.make_rooms(35, 60, 20))
    curses.curs_set(0)  # Hide cursor

    stdscr.clear()
    stdscr.refresh()

    map_window = curses.newwin(36, 69, 3, 5)  # Create a window for the map_d
    msg_window = curses.newwin(30, 60, 6, 74)  # Create a window for messages

    decorator.decorate(stdscr, 1)
    stdscr.refresh()
    stdscr.getch()

    stdscr.clear()
    decorator.decorate(stdscr, 3)
    stdscr.refresh()

    selected_hero = p.choose_player(stdscr, hero1, hero2, hero3)
    stdscr.refresh()
    stdscr.clear()

    mobs_killed = 0
    hero = selected_hero

    mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items[lvl], [])
    mapka.adjust_mobs_to_lvl(lvl, mobs1.copy(), mobs2.copy(), mobs3.copy())
    mapka.set_mobs_and_items_on_map()

    while True:
        user_input = stdscr.getkey()
        map_window.clear()
        msg_window.clear()
        mapka.show_stats(msg_window, mobs_killed, lvl)
        mapka.actor.show_eq(msg_window)
        moved = False
        if user_input == "KEY_UP":
            mobs_killed = mapka.actor.attack_with_key(mapka, mobs_killed, msg_window, "up")
            mapka.move_person(mapka.actor.x - 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_DOWN":
            mobs_killed = mapka.actor.attack_with_key(mapka, mobs_killed, msg_window, "down")
            mapka.move_person(mapka.actor.x + 1, mapka.actor.y)
            moved = True
        elif user_input == "KEY_LEFT":
            mobs_killed = mapka.actor.attack_with_key(mapka, mobs_killed, msg_window, "left")
            mapka.move_person(mapka.actor.x, mapka.actor.y - 1)
            moved = True
        elif user_input == "KEY_RIGHT":
            mobs_killed = mapka.actor.attack_with_key(mapka, mobs_killed, msg_window, "right")
            mapka.move_person(mapka.actor.x, mapka.actor.y + 1)
            moved = True
        elif user_input == "\n":
            if mapka.map_check(mapka.actor.x, mapka.actor.y) == "stairs" and not mapka.show_info(msg_window, 0):
                lvl += 1
                if lvl == 10:
                    decorator.decorate(stdscr,5)
                    msg_window.refresh()
                    stdscr.getch()
                    break
                else:
                    mapka.actor.level_up()
                    mapka = m.Map(maps[lvl][0], maps[lvl][1], maps[lvl][2], hero, items[lvl], [])
                    mapka.adjust_mobs_to_lvl(lvl, mobs1.copy(), mobs2.copy(), mobs3.copy())
                    mapka.set_mobs_and_items_on_map()
                    mobs_killed = 0
                    msg_window.refresh()
        elif user_input == "i":
            mapka.show_info(msg_window, 1)
        elif user_input == "b":
            hero.show_backpack(msg_window)
        elif user_input == "f":
            if mapka.check_if_item_to_collect():
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
        if moved:
            for mobs in mapka.mobs:
                if mobs.alive:
                    mobs.make_move(mapka, msg_window)
                msg_window.refresh()
        msg_window.refresh()
        mapka.remove_dead_mobs()
        mapka.map_printer2(map_window)
        msg_window.refresh()
        map_window.refresh()
        if not hero.alive:
            stdscr.clear()
            decorator.decorate(stdscr, 2)
            stdscr.refresh()
            break

    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
