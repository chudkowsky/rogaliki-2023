import random

import map_element as me



def generator(x, y):
    result = []
    tmp = []
    for i in range(x):
        tmp.clear()
        for j in range(y):
            tmp.append(me.Wall())
        if tmp:
            result.append(tmp.copy())
    return result


def make_rooms(x, y, num):
    result = generator(x, y)
    list_of_room_centers = []

    for i in range(num):
        if i<int(num/4):
            room_center_x = random.randint(1, int(x/2) - 1)
            room_center_y = random.randint(1, int(y/2) - 1)
            list_of_room_centers.append([room_center_x, room_center_y])
        elif int(num/4)<= i <int(num/2):
            room_center_x = random.randint(int(x/2), x - 1)
            room_center_y = random.randint(1, int(y/2) - 1)
            list_of_room_centers.append([room_center_x, room_center_y])
        elif int(num / 2) <= i < int(num / 4)*3:
            room_center_x = random.randint(1, int(x/2) - 1)
            room_center_y = random.randint(int(y/2), y - 1)
            list_of_room_centers.append([room_center_x, room_center_y])
        else:
            room_center_x = random.randint(int(x/2), x - 1)
            room_center_y = random.randint(int(y/2), y - 1)
            list_of_room_centers.append([room_center_x, room_center_y])

    # Create rooms
    for center in list_of_room_centers:
        center_x, center_y = center
        size = random.randint(4, 6)
        for i in range(center_x - int(size / 2), center_x + int(size / 2)):
            for j in range(center_y - int(size / 2), center_y + int(size / 2)):
                if 2 < i < x - 2 and 2 < j < y - 2:
                    result[i][j] = me.Floor()
    connect_rooms(result, list_of_room_centers)

    x1,y1 = list_of_room_centers[0]

    while not (0<x1<x and 0<y1<y and result[x1][y1].placeable == True ):
        x1,y1 = random.randint(0,x),random.randint(0,y)
    result[x1][y1] = me.Anvil()

    x1, y1 = list_of_room_centers[-1]

    while not (0 < x1 < x-1 and 0 < y1 < y-1 and result[x1][y1].placeable == True ):
        x1, y1 = random.randint(0, x), random.randint(0, y)
    result[x1][y1] = me.Stairs()
    return [result, x, y]


def connect_rooms(result, room_centers):
    room_centers.sort()
    for i in range(len(room_centers) - 1):
        room1_x, room1_y = room_centers[i]
        room2_x, room2_y = room_centers[i + 1]
        connect_centers(result, room1_x, room1_y, room2_x, room2_y)


def connect_centers(result, x1, y1, x2, y2):
    while x1 != x2 or y1 != y2:
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        for i in range(x1 - 1, x1 + 2):
            for j in range(y1 - 1, y1 + 2):
                if 0 < i < len(result)-1 and 0 < j < len(result[0])-1:
                    result[i][j] = me.Floor()

make_rooms(40,40,20)