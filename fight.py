def within_attacking_distance(map):
    player_position = (map.actor.x, map.actor.y)
    attacking_distance = map.actor.attacking_distance
    for i in range(1, 1 + attacking_distance):
        if map.map_check_mobs(player_position[0] + i, player_position[1])[0]:
            return True
        if map.map_check_mobs(player_position[0] - i, player_position[1])[0]:
            return True
        if map.map_check_mobs(player_position[0], player_position[1] + i)[0]:
            return True
        if map.map_check_mobs(player_position[0], player_position[1] - i)[0]:
            return True
    return False

def combat(hero, dog, flag):
    round_num = 1
    while hero.is_alive() and dog.is_alive():
        if (flag):
            print(f"Round {round_num}:")
        hero_attacked = hero.attack(dog, flag)
        if not dog.is_alive():
            if flag:
                print(f"{dog.name} has been defeated! {hero.name} wins!")
            break

        if hero_attacked:
            dog.attack(hero, flag)
            if not hero.is_alive():
                if (flag):
                    print(f"{hero.name} has been defeated! {dog.name} wins!")
                return True
        else:
            if (flag):
                print(f"{hero.name} has defeated {dog.name}!")
            return False
        round_num += 1
