def decorate(stdscr):
    f = open("decorations.txt","r",encoding='UTF-8')
    plik = f.readlines()

    for i,lines in enumerate(plik):
        stdscr.addstr(3+i,40,lines)

    f.close()

