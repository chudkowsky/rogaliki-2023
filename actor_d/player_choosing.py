from interface import decorator


def choose_player(stdscr, hero1, hero2, hero3):
    while True:
        stdscr.clear()
        decorator.decorate(stdscr, 3)
        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            selected_hero = hero1
            stdscr.addstr(f"Wybrałeś {hero1.name}")
            break  # Break out of the loop if a valid hero is selected
        elif choice == ord('2'):
            selected_hero = hero2
            break
        elif choice == ord('3'):
            selected_hero = hero3
            break
        elif choice == ord('i'):
            stdscr.clear()
            decorator.decorate(stdscr, 4)
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.addstr("Invalid choice. Press 1, 2, 3, or 'i' for more info.")

    return selected_hero
