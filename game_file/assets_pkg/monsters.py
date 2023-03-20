class Monster:
    def __init__(self, name, hp, dmg, special, desc):
        self.name = name
        self.hp = hp
        self.hp_reset = hp
        self.dmg = dmg
        self.special = special
        self.desc = desc

    def monster_hp_reset(self):
        self.hp = self.hp_reset


three_head_cat = Monster("Three Headed Cat", 500, 60, "ko_three_headed_cat",  "The Three headed cat was born naturally into this world, but quickly showed signs of malicious play from the beyond realms. Growing quickly, the three headed kitten became the size of an average cow within two months, before finishing at the size you see before you. The size of a goliath. Inexplicably, the natural lactose intolerance that house cats have has been amplified to gargantuan levels in this beast.")

lich_knight = Monster("Lich Knight", 250, 150, "ko_lich_knight",  "To become a lich is an incredible process that allows a soul to inhabit its own body not a living being, but instead as an undead host. This allows incredible longevity, and with dedication, amazing durability. However, lichdom comes mainly from magic and the consummation of souls, and without those a lich's power tends to diminish and become more like standard undead. This is a knight who dabbled in magic and achieved lichdom, before being captured for this arena. A terrifying corpse in black armor with a greatsword.")

hobgoblin_king = Monster("Hobgoblin King", 80, 30, "ko_hobgoblin_king",  "The king of the hobgoblins, a race of goblins unusually large, which means around the size of small humans instead of halflings. The king was offered to the arena for the purpose of glory for the hobgoblin people, as he is the strongest of them. He is a lean, toned being armed with leather armor and a simple sword, with the vengeance of his people driving his every move. Hobgoblins are not usually a strong threat, but he does look like he packs a punch.")

faerie_dragon = Monster("Faerie Dragon", 100, 200, "ko_faerie_dragon",  "A shockingly small creature, its size only makes it more dangerous. Although the size of a normal house cat, this creature has all of the tricks and attitude that comes of the fae realm. This means that it has magic and a bite that can bring down some massive beasts, plus it's small and nimble enough to evade most attacks from all but the most talented of fighters. Good thing you are! ")

cosmic_beast = Monster("Cosmic Beast", 500, 80, "ko_cosmic_beast",  "A mass of eyes, mouths, and tentacles made from what can only be described as living tar, this beast is summoned into the arena. You suspect this is what they meant when you heard a cult talking of the old gods, and now one is captured to slay or be slain for the entertainment of the masses. You better be prepared for the fight of and for your life.")

spine_porcupine = Monster("Spine, the Mutant Porcupine", 500, 80, "ko_spine_porcupine",  "This creature was apparently at one point just a normal porcupine. Now it more resembles an over muscular bear with a bad haircut and buck teeth. One way or another though, it's not happy and looks ready to fight anything despite everything. The paperwork in front of you states that this beast was a failed experiment for a new type of war beast that backfired and decimated the kingdom instead. Good riddance to anyone who thought this was a good idea.")

amalgam = Monster("Amalgam", 600, 20, "ko_amalgam",  "A pile of writhing flesh, it doesn't seem like its going to be much of a challenge. The real challenge is going to be wiping the chorus of screams, wails, and moans put forth by the horrendous monstrocity before you from your head. The came from a curse that was unleashed by a group of adventurers, and consumed any living thing it could touch for miles. The only thing keeping it contained now is the incredible walls that surround the arena.")

another_warrior = Monster("Another Warrior", 250, 120, "ko_another_warrior",
                          "This is another warrior, but something seems off. There is no life behind their eyes, but they aren't dead either. What happened? You notice they have an ax, one that seems to have been well used. There is nothing driving them though, nothing but the arena.")
