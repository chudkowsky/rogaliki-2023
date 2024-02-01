def decorate(stdscr, num):
    f1 = open("assets_d/starting_screan.txt", "r", encoding='UTF-8')
    f2 = open("assets_d/ending_screan.txt", "r", encoding='UTF-8')
    f3 = open("assets_d/choosing_player", "r", encoding='UTF-8')
    f4 = open("assets_d/info_player", "r", encoding='UTF-8')
    f5 = open("assets_d/winning_scream", "r", encoding='UTF-8')
    f6 = open("assets_d/controls_info", "r", encoding='UTF-8')
    if num == 1:
        plik1 = f1.readlines()
        for i, lines in enumerate(plik1):
            stdscr.addstr(3 + i, 40, lines)
    elif num == 2:
        plik2 = f2.readlines()
        for i, lines in enumerate(plik2):
            stdscr.addstr(3 + i, 40, lines)
    elif num == 3:
        plik3 = f3.readlines()
        for i, lines in enumerate(plik3):
            stdscr.addstr(3 + i, 40, lines)
    elif num == 4:
        plik4 = f4.readlines()
        for i, lines in enumerate(plik4):
            stdscr.addstr(3 + i, 20, lines)
    elif num == 5:
        plik5 = f5.readlines()
        for i, lines in enumerate(plik5):
            stdscr.addstr(3 + i, 40, lines)
    elif num == 6:
        plik6 = f6.readlines()
        for i, lines in enumerate(plik6):
            stdscr.addstr(lines)
    f1.close()
    f2.close()
