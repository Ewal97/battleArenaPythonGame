from assets_pkg.monsters import amalgam
from assets_pkg.monsters import another_warrior
from assets_pkg.monsters import cosmic_beast
from assets_pkg.monsters import faerie_dragon
from assets_pkg.monsters import hobgoblin_king
from assets_pkg.monsters import lich_knight
from assets_pkg.monsters import spine_porcupine
from assets_pkg.monsters import three_head_cat
from assets_pkg.weapons import a_pile_of_china
from assets_pkg.weapons import a_sword
from assets_pkg.weapons import ancient_dagger
from assets_pkg.weapons import bag_of_iron_spikes
from assets_pkg.weapons import bag_of_marbles
from assets_pkg.weapons import battleaxe_from_hell
from assets_pkg.weapons import blacksmiths_hammer
from assets_pkg.weapons import cheese_on_a_stick
from assets_pkg.weapons import divine_dagger
from assets_pkg.weapons import found_item_mace
from assets_pkg.weapons import granny_cookies
from assets_pkg.weapons import great_hammer
from assets_pkg.weapons import mysterious_sword
from assets_pkg.weapons import severing_scissors
from assets_pkg.weapons import spike_of_quartz
from assets_pkg.weapons import sword_of_the_mages
from assets_pkg.battle_func import battle_func
import random

high_score = {"Player": "Finished Health"}


class Player:

    def __init__(self, hp, dmg, weapon_name, special, desc, breakable, special_txt):
        self.hp = hp
        self.hp_reset = hp
        self.dmg = dmg
        self.weapon_name = weapon_name
        self.special = special
        self.desc = desc
        self.breakable = breakable
        self.special_txt = special_txt
        self.name = "A Warrior"
        self.is_dead = False

    def broke_reset(self):
        if self.breakable == True:
            print("\nThe weapon cannot see another fight, it is unusable.")
            self.dmg = 30
            self.weapon_name = "Bare Fists"
            self.special = "none"
            self.desc = "You have your bare fists before you, the only weapon you can consistently rely on."
            self.breakable = False
            self.special_txt = ""
        else:
            print("Your weapon lasts to see another fight.")

    def game_reset(self):
        self.hp = self.hp_reset
        self.dmg = 30
        self.weapon_name = "Bare Fists"
        self.special = "none"
        self.desc = "You have your bare fists before you, the only weapon you can consistently rely on."
        self.breakable = False
        self.special_txt = ""

    def health_potion(self):
        health_amount = (50 * (random.randint(1, 5)))
        if health_amount == 50:
            self.hp += health_amount
            print(
                "You find a small health potion waiting for you.\nYour health is now at " + str(self.hp))
        elif health_amount == 100:
            self.hp += health_amount
            print(
                "You find a health potion waiting for you.\nYour health is now at " + str(self.hp))
        elif health_amount == 150:
            self.hp += health_amount
            print(
                "You find a medium health potion waiting for you.\nYour health is now at " + str(self.hp))
        elif health_amount == 200:
            self.hp += health_amount
            print(
                "You find a large health potion waiting for you.\nYour health is now at " + str(self.hp))
        elif health_amount == 250:
            self.hp += health_amount
            print(
                "You find a grand health potion waiting for you.\nYour health is now at " + str(self.hp))
        else:
            self.hp += health_amount
            print("You found a potion beyond reality, congrats!")


player = Player(250, 30, "Bare Fists", "none",
                "You have your bare fists before you, the only weapon you can consistently rely on.", False, "")


play = True

while True:


    monsters_list = [amalgam, cosmic_beast, another_warrior, faerie_dragon,
                     hobgoblin_king, lich_knight, spine_porcupine, three_head_cat]
    for x in monsters_list:
        x.monster_hp_reset()

    weapons_list = [a_pile_of_china, a_sword, ancient_dagger, bag_of_iron_spikes, bag_of_marbles, battleaxe_from_hell, blacksmiths_hammer, cheese_on_a_stick,
                    divine_dagger, found_item_mace, granny_cookies, great_hammer, mysterious_sword, severing_scissors, spike_of_quartz, sword_of_the_mages]

    random.shuffle(monsters_list)
    monster1 = monsters_list[1]
    monster2 = monsters_list[2]
    monster3 = monsters_list[3]
    monster4 = monsters_list[4]
    monster5 = monsters_list[5]
    
    print("High Scores!")
    for x in high_score:
        print(x, "  |  ", high_score[x])

    game_monster_list = [monster1, monster2, monster3, monster4, monster5]
    while True:
        player.name = input("Name Your Character: ")
        if len(player.name) >= 3 and len(player.name) <= 15:
            break
        else:
            print("Name must be between 3 and 15 characters!\n")

    print("\nYou are the newest warrior to enter the arena, you have no recollection of how you got here, but know you have to fight to leave.\nWelcome to battle", player.name + "!")

    for boss in game_monster_list:
        random.shuffle(weapons_list)
        weapon1 = weapons_list.pop(0)
        weapon2 = weapons_list.pop(0)
        weapon3 = weapons_list.pop(0)
        if player.breakable == True:
            player.broke_reset()
        print("\nYou are given some information of the monster you will face:\n" + boss.name +
              ") Health Points:", str(boss.hp), "Strength:", str(boss.dmg) + "\nDescription: " + boss.desc)

        print("\nA set of three weapons lays on a table before you.\n\n1)", weapon1.name + "| Strength:", str(weapon1.dmg), "\nDescription:", weapon1.desc, "\n\n2)",
              weapon2.name + "| Strength:", str(weapon2.dmg), "\nDescription:", weapon2.desc, "\n\n3)", weapon3.name + "| Strength:", str(weapon3.dmg), "\nDescription:", weapon3.desc)
        if player.weapon_name == "Bare Fists":
            print("\n4) You have you reliable fists too! Strength:",
                  str(player.dmg), "\nDescription:", player.desc)
        else:
            print("\n4) You have the weapon from the previous battle in your hand! Strength:", str(
                player.dmg), "\nDescription:", player.desc)
    #    print("\n4) You have the weapon from the previous battle in your hand! Strength:", str(player.dmg),"\nDescription:", player.desc if (player.weapon_name != "Bare Fists") else "\n4) You have you reliable fists too! Strength:", str(player.dmg),"\nDescription:", player.desc) ({[failed code i am keeping in for reference]})
        while True:
            user_input = input("\nChoose a weapon: ")
            if user_input == "1":
                player.dmg = weapon1.dmg
                player.weapon_name = weapon1.name
                player.special = weapon1.special
                player.desc = weapon1.desc
                player.breakable = weapon1.breakable
                player.special_txt = weapon1.special_txt
                break
            elif user_input == "2":
                player.dmg = weapon2.dmg
                player.weapon_name = weapon2.name
                player.special = weapon2.special
                player.desc = weapon2.desc
                player.breakable = weapon2.breakable
                player.special_txt = weapon2.special_txt
                break
            elif user_input == "3":
                player.dmg = weapon3.dmg
                player.weapon_name = weapon3.name
                player.special = weapon3.special
                player.desc = weapon3.desc
                player.breakable = weapon3.breakable
                player.special_txt = weapon3.special_txt
                break
            elif user_input == "4":
                break
            else:
                print("\nPlease choose valid input!!")
        battle_func(player, boss)
        if player.is_dead == True:
            print("As your soul leaves your body, you find it being forcefully held back, as ethereal strings come and attach to your body. You are not allowed to leave this arena until permitted, even in the case of death.")
            break
        else:
            player.health_potion()
    if player.is_dead == False:
        print("\nYou leave the arena, a new champion of the Ages!! Congratulations on surviving!")
        high_score[player.name] = player.hp
    while True:
        play_again = input("\nWant to play again?\nYes or No? ")
        if play_again.lower() == "yes" or play_again.lower() == "y":
            player.breakable = True
            player.game_reset()
            player.is_dead = False
            break
        elif play_again.lower() == "no" or play_again.lower() == "n":
            print("\nThanks for playing!!")
            exit()
        else:
            print("\nPlease choose a valid option!")

    """     print(player.dmg, "|", player.weapon_name, "|", player.special, "|",
            player.desc, "|", str(player.breakable), "|", player.special_txt)
            
            test code to make sure everything initialized correctly
    """
