
from units import *

attackers = []
#attackers += [ squig, g1, g2 ]

#attackers += [ g1 ]
attackers += [ sq1, g1, ob1, ork_hero1 ]
#attackers += [ sq1, sq2, sq3, sq4, sq5 ]

#attackers += [ sq1, sq2 ]
#attackers += [ g1, g2, g3, g4 ]
#attackers += [ g5 ]
#attackers += [ ob1, ob2, ob3, ob4, ob5 ]
#attackers += [ ork_hero1, ork_hero2, ork_hero3 ]
#attackers += [ ork_shaman ]

##### special grumlok
#grumlok.a=5
#grumlok.i=5
#grumlok.ws=4
#grumlok.t=6
#grumlok.w=3 # ork maximum wounds
#grumlok.w=4 # witch +1W potion
#grumlok.s=4 # ork maximum strength
#grumlok.s=5 # witch +1S potion
#grumlok._as=3 # well ard + hemd + light armor = 3AS
#grumlok._as=2 # well ard + hemd + light armor = 3AS + shield/well ard +1AS
#grumlok._as=1 # well ard + hemd + light armor = 3AS + war boar

## two axes
#grumlok.weapon[0]["name"] = "axe"
#grumlok.weapon[0]["s"] = 0
#grumlok.weapon[0]["as"] = -1
#grumlok.weapon[1]["name"] = "axe"
#grumlok.weapon[1]["toHitOffhand"] = 2 # like two handed master
#grumlok.weapon[1]["s"] = 0
#grumlok.weapon[1]["as"] = -1

# two obsidian axes
#grumlok.weapon[0]["name"] = "obsidian axe"
#grumlok.weapon[0]["s"] = 1
#grumlok.weapon[0]["as"] = -1
#grumlok.weapon[1]["name"] = "obsidian axe"
#grumlok.weapon[1]["toHitOffhand"] = 2 # like two handed master
#grumlok.weapon[1]["s"] = 1
#grumlok.weapon[1]["as"] = -1

# two-handed weapon
#grumlok.weapon[0]["name"] = "two-handed axe"
#grumlok.weapon[0]["s"] = 2
#grumlok.weapon[0]["as"] = 0

# obsidian two-handed weapon
#grumlok.weapon[0]["name"] = "obsidian two-handed axe"
#grumlok.weapon[0]["s"] = 3
#grumlok.weapon[0]["as"] = 0

# remove second weapon
#del grumlok.weapon[-1] # remove the offhand

## special skills
#grumlok.hate = True
#grumlok.firstRoundToHitAdd = 2
#grumlok.ardEad = True
#grumlok.resilient = True
#grumlok.stepaside = True # not on war boar
#grumlok.mightyblow = True
#grumlok.striketoinjure = True
#grumlok.parry = True # parry with axes skill
#grumlok.parryImproved = True
#####

#attackers += [ chaos_warr ]
#attackers += [ belandysh ]
#attackers += [ copy.deepcopy(champ_of_chaos) ]
attackers += [ grumlok ]
#attackers += [ war_boar ]
#attackers += [ troll ]
#attackers += [ troll, mutant, pit_ogre, beastmen, ork_shaman, dwarf1, centigor ]

#target = chaos_dragon
#target = belandysh
#target = champ_of_chaos
#target = chaos_warr
#target = centigor
#target = beastmen
#target = pit_ogre
#target = beastmen_hound
target = troll

