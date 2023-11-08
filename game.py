import os
import map as m


def refresh():
    os.system('cls')

mapa1 = [['#', '#', '#', '#', '#'],
            ['#', '_', '_', '#', '#'],
            ['#', '@', '_', '&', '#'],
            ['#', '#', '&', '#', '#']
            ]
mapka = m.Map(mapa1, 4, 5)

mapka.map_printer()
refresh()
