def battle_func(player, monster):
    while True:
        if player.special == monster.special:
            print("\n" + player.special_txt)
            break
        else:
            print("\nThe Battle begins!!")
            while True: 
                if player.hp > 0 and monster.hp > 0:
                    monster.hp = (monster.hp - player.dmg)
                    print("You hit the", monster.name, "with your", player.weapon_name, "for", str(player.dmg), "damage!")
                    if monster.hp <= 0:
                        print("You have defeated the monster!")
                        break
                    else: 
                        player.hp -= monster.dmg
                        print("The Monster hits you for", str(monster.dmg), "damage!")
                        if player.hp <= 0:
                            print("You have been defeated!")
                            player.is_dead = True
                            break
                        else:
                            print("You have", str(player.hp), "Health Points left, while the monster has", str(monster.hp), "remaining.")

                elif player.hp > 0 and monster.hp <= 0:
                    print("You have defeated the monster!")
                    break
                else:
                    print("You have been defeated!")
                    player.is_dead = True
                    break
            break
    print("\nThe battle ends!")


