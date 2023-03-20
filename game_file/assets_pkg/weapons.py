class Weapon:
    def __init__(self, name, dmg, special, breakable, desc, special_txt):
        self.name = name
        self.dmg = dmg
        self.special = special
        self.breakable = breakable
        self.desc = desc
        self.special_txt = special_txt


cheese_on_a_stick = Weapon("Cheese on a Stick", 5, "ko_three_headed_cat", True, "It is what it says it is. It's a decent piece of a hard aged cheese attached to a stick in some sort of an improvised mace.",
                           "To your amazement, when you lobbed the cheese stick at the beast, it immediately ate it with a ferocity like a housecat with its favorite treat. However, this was its undoing. Within seconds, and before it could react, the lactose intolerance took over, disgusting the entire arena with [redacted content]. After a minute the beast slumped over from sheer exhaustion, defeated. You, disgusted, question your reality and prepare for your next battle.")

divine_dagger = Weapon("Divine Dagger", 80, "ko_lich_knight", False, " A dagger created in unison by the followers of all great gods, given the divine power to smite all unnatural evil.",
                       "The lich made a mistake when it decided to not focus on magic. Susceptible to divine intervention now, as the knife slashes the knight, its flesh begins to glow and purify into dust, quickly leaving the former horror as a pile of dust and armor on the ground of the arena.")

great_hammer = Weapon("Great Hammer", 150, "ko_hobgoblin_king", False, "This simply is a massive hammer. Its head is the size of a loaf of bread and solid iron, and the handle is long and sturdy, letting you get a good grip to smash everything.",
                      "The head of the hammer is bigger than the poor hobgoblin's body, and definitely heavier than the whole creature before you. With a heavy heart for the poor thing, you swing with perfect timing to hopefully end this swiftly. And you succeeded in a merciful end to a fighter who entered the wrong battle, with the heavy thud confirming it. Rest in Peace strange little king.")

bag_of_iron_spikes = Weapon("A Bag of Iron Spikes", 20, "ko_faerie_dragon", True, "As it says, it's a bag of iron spikes. They kind of resemble a children's game you saw other children play when you had to do chores outside for your training. But, like really sharp, and really inconvenient.",
                            "An occurrence came to you at the beginning of this battle. Those who hail from the fae realm cannot touch iron, for it poisons them. In a brilliant move against such a small foe, you throw the entire bag in a rain of iron towards the small dragon, and to your delight it starts burning immediately as if the spikes had been made of acid magic. The battle ends in cheers of your ingenuity.")

sword_of_the_mages = Weapon("Sword of the Mages", 100, "ko_cosmic_beast", False, "This sword resembles one you came across years ago. Was it the one from the dragon's hoard, the one made by a cult of wizards, or was it the prized possession of the really nice tavern owner that was knocking on death's door? Anyway, it's a good sword with some magic.",
                            "It came to you in the moment. This is the sword the cult designed specifically to defeat an old god to prove your power to the Council of the Beasts. With a single flying slash, you slash a glowing wound in the side of the beast. The light from within starts spreading like a disease, consuming the whole beast before evaporating into embers. You have won, and may have proven yourself to the council. But, you aren't sure how to apply. Oh well.")

spike_of_quartz = Weapon("Spike of Quartz", 60, "ko_spine_porcupine", True, "It may be the Earth's glass, but it should pack a punch for at least one round. Hopefully.",
                         "The mutant creature is terrifying, but as it turns out, was also mutated by corruption. Seems that natural quartz is somewhat good at purifying, and decorrupting, because as soon as the point pierced the skin of the beast, the beast starting thrashing and writhing in agony. With a mighty leap, you push the spike with all of your might, burying it in the side of the porcupine. The form quickly starts shrinking back to the original size it should have been, and spews blood in every direction as it thrashes about trying to shake off the spike. Too bad there wasn't a nicer way to do this, or a way to let the porcupine return to nature. But you are pretty sure the arena wouldn't let you leave the creature alive even if you could save it. Rest in peace little one, you didn't deserve any of it.")

granny_cookies = Weapon("Granny Apollo's Original Chocolate Chip Cookies!", (-10), "ko_amalgam", True, "Granny Apollo's original recipe brings in her love and care to refuel you, and keep you ticking. Eating one gives the amazing love and warmth that only a divine granny can bring",
                        "Although these aren't really a weapon, it seems to be effective here! When you started tossing cookies into the many mouths of the amalgam before you, Granny's love started breaking apart the amalgam into its base pieces, leaving a group of very confused people and animals standing in the arena, and a small goo blob that started it all. You finish the battle with the bottom of your boot, smashing the blob into the sand, never to amalgam again.")

severing_scissors = Weapon("Severing Scissors", 25, "ko_another_warrior", False, "These scissors say they are designed to cut any thread it comes across, and helps you see the threads that are invisible. Maybe this makes more sense when you are a tailor.",
                           "The warrior before you has strings that are connecting to its limbs, like a giant marionette. It occurs to you that you know what to do. You launch yourself across the battlefield to get at the strings before the warrior has a chance to react. The scissors grab the ethereal strings with ease, severing them. The warrior seems to fall over into a pile, now dead. The soul was no longer controlling the body, and now is finally free to rest in peace. You wonder how they got like this.")

a_sword = Weapon("A-Sword", 120, "none", False,
                 "You have never seen a weapon like this, its two swords fused into the shape of an A, with a cross bar of another blade making the cross bar. Strange…", "")

battleaxe_from_hell = Weapon("Battleaxe from Hell", 200, "none", False,
                             "This Axe appears to be made from the very fabric of the underworld. Glowing with the embers of hatred and shining spite and evil substantiating the weapon itself. This should be fun.", "")

bag_of_marbles = Weapon("Bag of Marbles and a Slingshot", 40, "none", True,
                        "Literally a bag of glass children's marbles and a slingshot. It may seem random and useless, but glass is hard as stone, and shatters into a wonderful spray of shrapnel. Not the most powerful, but you can make it work.", "")

blacksmiths_hammer = Weapon("Blacksmith's Hammer", 100, "none", False,
                            "The small can be mighty. This hammer is proof of this. A one handed weapon that packs a punch, this small hammer is usually used to beat metal into submission. You know you can utilize it well.", "")

a_pile_of_china = Weapon("A Pile of Green China", 35, "none", True, "This looks like a pile of weird dishes the bald old lady in the village loved collecting. Never made sense why she kept collecting them once she got sick, but one way or another. There were a lot of green dishes. Now you can use them to destroy a beast in the arena, just no way they are surviving after.", "")

mysterious_sword = Weapon("Mysterious Sword", 110, "none", False, "It seems suspiciously normal, a complete anomaly amongst the insanity you have found otherwise in this place. This sword is literally just a normal sword, but somehow it seems off. Like the feeling you get when a training dummy was left in your room and it seemed to be staring at you.", "")

ancient_dagger = Weapon("Ancient Dagger", 60, "none", True, "Normally you say ancient dagger like it’s a mysterious ancient relic full of power. Not this one. This one is about the fall apart, and is only being held together with rust and desperation. Thankfully, it seems like it can do some damage, but it is not going to hold up more than one more round.", "")

found_item_mace = Weapon("Mace Made of Found Items", 100, "none", False,
                         "Somehow, somewhere, someone took a bunch of random sharp objects, and figured out how to attach them to a heavy metal ball. As much as it looks like a child’s art project, it will work.", "")

weapon_default = Weapon("Bare Fists", 30, "none", False,
                         "You have your bare fists before you, the only weapon you can consistently rely on.", "")
