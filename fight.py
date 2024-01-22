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
