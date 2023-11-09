import map_element as m


def map_parser(directory):
    f = open(directory, "r")
    bufor = f.read()
    f.close()
    result = []
    tmp = []
    for character in bufor:
        if character == "#":
            tmp.append(m.Wall())
        if character == "_":
            tmp.append(m.Floor())
        if character == "\n":
            result.append(tmp.copy())
            tmp = []
    if tmp:
        result.append(tmp.copy())

    return result
