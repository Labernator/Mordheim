
from simu_unit import *
from units import *

#####
troll = Unit()
troll.regeneration = False

#####
centigor = Unit()
centigor.name = "centigor"
centigor.t = 4
centigor.s = 4
centigor.w = 1
centigor.a = 1
centigor.ws = 4
centigor._as = 0
centigor.i = 2
centigor.weapon = [
    copy.deepcopy(club),
    copy.deepcopy(club_offhand),
    copy.deepcopy(foot)
]

#####
pit_ogre = Unit()
pit_ogre.name = "pit fighter ogre"
pit_ogre.ws = 3
pit_ogre.s  = 4
pit_ogre.t  = 4
pit_ogre.w  = 3
pit_ogre.i  = 3
pit_ogre.a  = 2
pit_ogre._as = 4
pit_ogre.weapon = [
	copy.deepcopy(dagger),
	copy.deepcopy(dagger_offhand),
]

#####
pit_king = Unit()
pit_king.name = "pit fighter king"
pit_king.ws = 4
pit_king.s  = 4
pit_king.t  = 4
pit_king.w  = 2
pit_king.i  = 4
pit_king.a  = 2
pit_king._as = 4
pit_king.rabbitsFoot = True
pit_king.resilient = True
pit_king.weapon = [
	copy.deepcopy(flail),
]
# bulding beaceps
pit_king.weapon[0]["firstRoundSAdd"] = 0
pit_king.weapon[0]["s"] = 2

#####
ogre_bodyguard = Unit()
ogre_bodyguard.name = "ogre bodyguard"
ogre_bodyguard.ws = 3
ogre_bodyguard.s  = 4
ogre_bodyguard.t  = 4
ogre_bodyguard.w  = 3
ogre_bodyguard.i = 3
ogre_bodyguard.a  = 2
ogre_bodyguard._as = 5
ogre_bodyguard.parry = True
ogre_bodyguard.helmet = True
ogre_bodyguard.weapon = [
	copy.deepcopy(axe),
	copy.deepcopy(sword_offhand),
]

ogre_slavemaster = copy.deepcopy(ogre_bodyguard)
ogre_slavemaster.i = 4

#####
war_boar = Unit()
war_boar.name = "binky tha war boar"
war_boar.ws = 3
war_boar.s = 3
war_boar.t = 4
war_boar.w = 1
war_boar.i = 5
war_boar.a = 1
war_boar._as = 5
war_boar.cantBeAttacked = True
war_boar.weapon = [
	copy.deepcopy(animal_attack)
]

#####
grumlok = Unit()
grumlok.name = "Grumlok"
grumlok.bs = 4
grumlok.rs = 4
grumlok.ws = 4
grumlok.s  = 4
grumlok.t  = 4
grumlok.w  = 1
grumlok.a  = 2
grumlok._as = 4
grumlok.i = 4
grumlok.helmet = True
grumlok.luckyCharm = True
grumlok.rabbitsFoot = True
grumlok.stepaside = True # not on war boar
grumlok.parry = True # parry with axes skill
grumlok.parryImproved = True # campaign progress
#grumlok.quickShot = True
grumlok.weapon = [
    copy.deepcopy(axe),
    copy.deepcopy(sword_offhand)
]

##### special grumlok - max ork stats
grumlok2 = copy.deepcopy(grumlok)
grumlok2.name = "Grumlok 2"
grumlok2.a=4  # +3A
grumlok2.i=5  # +2I
grumlok2.ws=6 # +2WS
grumlok2.t=5  # +1T
grumlok2.w=3  # ork maximum wounds
#grumlok2.w=4 # witch +1W potion
grumlok2.s=4 # ork maximum strength
#grumlok2.s=5 # witch +1S potion
#grumlok2._as=3 # well ard + hemd + light armor = 3AS
#grumlok2._as=2 # well ard + hemd + light armor = 3AS + shield
#grumlok2._as=1 # well ard + hemd + light armor = 3AS + war boar
## two axes with two-handed master
#grumlok2.weapon[1]["toHitOffhand"] = 2 # like two handed master

# halberd
#grumlok2.weapon = [ copy.deepcopy(dark_steel_halberd) ]
#grumlok2.weapon[0]["s"] = 2 # dark venom tainted halberd
#grumlok2.parry = False
#grumlok2.parryImproved = False

# axe & sword
grumlok2.weapon = [
    copy.deepcopy(axe),
    copy.deepcopy(sword_offhand)
]
grumlok2.weapon[0]["s"] = 1 # dark venom
grumlok2.weapon[0]["stunnedMin"] = 2 # dark steel axe
#grumlok2.weapon[0]["toHitAdd"] = 0 # cold metal
#grumlok2.weapon[0]["toInjuryRoll"] = 0 # ???
grumlok2.weapon[1]["s"] = 1 # dark venom
#grumlok2.weapon[1]["toHitAdd"] = 1 # cold metal sword

# two obsidian axes
#grumlok2.weapon[0]["type"] = "obsidian axe" # 20gc rare 12
#grumlok2.weapon[0]["s"] = 1
#grumlok2.weapon[0]["as"] = -1
#grumlok2.weapon[1]["type"] = "obsidian axe" # 20gc rare 12
#grumlok2.weapon[1]["toHitOffhand"] = 2 # like two handed master
#grumlok2.weapon[1]["s"] = 1
#grumlok2.weapon[1]["as"] = -1

# two-handed weapon
#grumlok2.weapon[0]["name"] = "two-handed axe"
#grumlok2.weapon[0]["s"] = 2
#grumlok2.weapon[0]["as"] = 0

# obsidian two-handed weapon
#grumlok2.weapon[0]["name"] = "obsidian two-handed axe"
#grumlok2.weapon[0]["s"] = 3
#grumlok2.weapon[0]["as"] = 0

# remove second weapon
#del grumlok2.weapon[-1] # remove the offhand

## special skills
grumlok2.hate = True # campaign progress
#grumlok.hate = False
grumlok2.firstRoundToHitAdd = 2 # campaign progress
#grumlok2.ardEad = True
grumlok2.resilient = True
grumlok2.mightyblow = True
grumlok2.striketoinjure = True
#####

#####
ork_shaman = Unit()
ork_shaman.name = "Wogga"
ork_shaman.bs = 0 # on diff 9 d3 hits
ork_shaman.rs = 4
ork_shaman.ws = 4
ork_shaman.s  = 3
ork_shaman.t  = 3 # chest wound
ork_shaman.w  = 2
ork_shaman.i = 3
ork_shaman.a = 1
ork_shaman._as = 0
ork_shaman.magicUser = True
ork_shaman.luckyCharm = True
ork_shaman.rabbitsFoot = True
ork_shaman.weapon = [
    copy.deepcopy(clubba),
    copy.deepcopy(dagger_offhand),
]
ork_shaman.luckyCharm = True

#####
ork_hero = Unit()
ork_hero.name = "ork hero"
ork_hero.ws = 4
ork_hero.s = 3
ork_hero.t = 4
ork_hero.w = 1
ork_hero.i = 3
ork_hero.a = 1
ork_hero._as = 0
ork_hero.weapon = [
	copy.deepcopy(hand_weapon),
	copy.deepcopy(dagger_offhand),
]

ork_hero1 = copy.deepcopy(ork_hero)
ork_hero1.name = "Grommok (Big'Un)"
ork_hero1.bs = 3
ork_hero1.rs = 4
ork_hero1.ws = 4
ork_hero1.s = 4
ork_hero1.t = 4
ork_hero1.w = 1
ork_hero1.i = 3
ork_hero1.a = 1
ork_hero1._as = 5 # light armour
ork_hero1.luckyCharm = True
#ork_hero1.quickShot = True
ork_hero1.weapon[0] = copy.deepcopy(axe)

ork_hero2 = copy.deepcopy(ork_hero)
ork_hero2.name = "Karhag (Big'Un)"
ork_hero2.bs = 3
ork_hero2.rs = 4
ork_hero2.ws = 4
ork_hero2.s = 3
ork_hero2.t = 4
ork_hero2.w = 1
ork_hero2.i = 3
ork_hero2.a = 2
ork_hero2._as = 5
ork_hero2.luckyCharm = True
#ork_hero2.quickShot = True
ork_hero2.weapon = [
	copy.deepcopy(axe),
	copy.deepcopy(hand_weapon_offhand)
]

ork_hero3 = copy.deepcopy(ork_hero)
ork_hero3.name = "Ug'Lash (Ork boy hero)"
ork_hero3.bs = 3
ork_hero3.rs = 4
ork_hero3.ws = 4
ork_hero3.s = 3
ork_hero3.t = 4
ork_hero3.w = 2
ork_hero3.i = 4
ork_hero3.a = 1
ork_hero3.luckyCharm = True
ork_hero3._as = 5
ork_hero3.weapon = [
	copy.deepcopy(axe),
	copy.deepcopy(dagger_offhand)
]

ork_hero4 = copy.deepcopy(ork_hero)
ork_hero4.name = "Rog'Rogg (Ork boy hero)"
ork_hero4.bs = 3
ork_hero4.rs = 4
ork_hero4.ws = 4
ork_hero4.s = 3
ork_hero4.t = 5
ork_hero4.w = 1
ork_hero4.i = 2
ork_hero4.a = 1
ork_hero4._as = 6
ork_hero4.weapon = [
	copy.deepcopy(axe),
	copy.deepcopy(dagger_offhand)
]

#####
squig = Unit()
squig.name = "squig"
squig.t = 3
squig.s = 4
squig.ws = 4
squig._as = 0
squig.w = 1
squig.a = 1
squig.i = 4
squig.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
squig.weapon = [
	copy.deepcopy(yaw)
]
####
sq1 = copy.deepcopy(squig)
sq1.name = "squig 1"
sq2 = copy.deepcopy(squig)
sq2.name = "squig 2"
sq3 = copy.deepcopy(squig)
sq3.name = "squig 3"
sq4 = copy.deepcopy(squig)
sq4.name = "squig 4"
sq5 = copy.deepcopy(squig)
sq5.name = "squig 5"

#####
ob1 = Unit()
ob1.name = "Blau (Ork boy)"
ob1.bs = 0
ob1.ws = 4
ob1.s = 3
ob1.t = 4
ob1.w = 1
ob1.i = 3
ob1.a = 2
ob1._as = 6
# first weapon
ob1.weapon = [
    copy.deepcopy(hand_weapon),
    copy.deepcopy(dagger_offhand)
]
####
ob2 = copy.deepcopy(ob1)
ob2.name = "Pink (Ork boy)"
ob2.bs = 0
ob2.ws = 3
ob2.s = 3
ob2.t = 4
ob2.w = 1
ob2.i = 2
ob2.a = 2
ob2._as = 0
####
ob3 = copy.deepcopy(ob1)
ob3.name = "Orange (Ork boy)"
ob3.bs = 0
ob3.ws = 3
ob3.s = 3
ob3.t = 4
ob3.w = 1
ob3.i = 2
ob3.a = 1
ob3._as = 0
####
ob4 = copy.deepcopy(ob2)
ob4.name = "Oggrot (Ork boy 5)"
ob4.i = 2

####
g1 = Unit()
g1.name = "goblin 1"
g1.bs = 3
g1.rs = 3
g1.ws = 2
g1.s = 3
g1.t = 3
g1.w = 1
g1.i = 3
g1.a = 1
g1._as = 0
g1.state = 0
g1.weapon = [
	copy.deepcopy(dagger),
	copy.deepcopy(dagger_offhand)
]
#
g2 = copy.deepcopy(g1)
g2.name = "goblin 2"
#
g3 = copy.deepcopy(g1)
g3.name = "goblin 3"
#
g4 = copy.deepcopy(g1)
g4.name = "goblin 4"
#
g5 = copy.deepcopy(g1)
g5.name = "goblin 5"
g5.i = 3
g5.weapon = [
	copy.deepcopy(spear)
]

#####
chaos_warr = Unit()
chaos_warr.name = "Chaos warrior"
chaos_warr.ws=6
chaos_warr.s=4
chaos_warr.t=4
chaos_warr.w=1
chaos_warr.i=6
#chaos_warr.a=2
chaos_warr.a=3 # frenzy + 4+ magic save
#chaos_warr._as=4 # heavy armor
chaos_warr._as=3 # heavy armor + shield
chaos_warr.helmet=True
chaos_warr.parry=False # sword only
chaos_warr.weapon = [
    copy.deepcopy(two_handed)
]

#####
goblin_leader = Unit()
goblin_leader.name="goblin leader"
goblin_leader.ws=3
goblin_leader.s=3
goblin_leader.t=3
goblin_leader.w=1
goblin_leader.i=4
goblin_leader.a=1
goblin_leader._as=4 # light armour + shield
goblin_leader.weapon = [
	copy.deepcopy(bosspole)
]

#####
goblin_leader2 = Unit()
goblin_leader2.name="goblin leader 2"
goblin_leader2.ws=5 # +2ws
goblin_leader2.s=4  # +1s
goblin_leader2.t=4  # +1t
goblin_leader2.w=3  # +2w
goblin_leader2.i=6  # +2i
goblin_leader2.a=4  # +3a
#goblin_leader2._as=6 # mount
#goblin_leader2._as=5 # mount + shield
#goblin_leader2._as=4 # shield + light armor
goblin_leader2._as=3 # mount + shield + light armor
#goblin_leader2.toHitAdd = 1 # mushroom chef
#goblin_leader2.s = 4 + 1 # mushroom chef
#goblin_leader2.a = 4 + 1 # mushroom chef
#goblin_leader2.stepaside = True # not on mount - or create forest goblin special skill
#goblin_leader2.striketoinjure = True # ccombat skill
goblin_leader2.hate = True
goblin_leader2.firstRoundToHitAdd = 2 # campaign progress
#goblin_leader2.t=4 + 2 # mushroom steroids
#goblin_leader2.a=4 + 1 # mushroom steroids
goblin_leader2.parry = True # sword or parry with axes skill
goblin_leader2.parryImproved = True # scourge of the realm achievment
#goblin_leader2.resilient = True # strength skill
#goblin_leader2.mightyblow = True # strength skill
goblin_leader2.luckyCharm = True
goblin_leader2.weapon = [
	#copy.deepcopy(bosspole)
        #copy.deepcopy(sword)
        copy.deepcopy(axe)
]
goblin_leader2.weapon[0]["s"] = 1 # dark venom
#goblin_leader2.weapon[0]["as"] = -2 # gromril weapon

#####
giantic_spider = Unit()
giantic_spider.name="giantic spider"
giantic_spider.ws=3
giantic_spider.s=5
giantic_spider.t=5
giantic_spider.w=3
giantic_spider.i=4
giantic_spider.a=2
giantic_spider._as=0
giantic_spider.cantBeAttacked = True # the oponent decides only for shooting
giantic_spider.stunnedMin=2
giantic_spider.stunnedMax=4
giantic_spider.weapon = [
	copy.deepcopy(giantic_spider_yaw)
]

#####
giant_spider = Unit()
giant_spider.name="giant spider"
giant_spider.ws=3
giant_spider.s=4
giant_spider.t=3
giant_spider.w=1
giant_spider.i=4
giant_spider.a=1
giant_spider._as=0
giant_spider.cantBeAttacked = True # the opponent always hit the hero
giant_spider.weapon = [
	copy.deepcopy(giant_spider_yaw)
]

#####

goblins = []
for i in range(11): # set the amount of goblins to create here
    goblins.append(copy.deepcopy(g1))
    goblins[i].name = "goblin " + str(i)
    goblins[i].bs = 4
    goblins[i].rs = 4

goblin_hero1 = copy.deepcopy(goblins[0])
goblin_hero1.name = "goblin hero 1"
# remove second weapon
del goblin_hero1.weapon[-1] # remove the offhand
goblin_hero2 = copy.deepcopy(goblin_hero1)
goblin_hero2.name = "goblin hero 2"
goblin_hero3 = copy.deepcopy(goblin_hero1)
goblin_hero3.name = "goblin hero 3"
goblin_hero3.weapon = [ copy.deepcopy(bosspole) ]

goblin_shaman = Unit()
goblin_shaman.name = "goblin shaman"
goblin_shaman.ws = 2
goblin_shaman.s = 3
goblin_shaman.t = 3
goblin_shaman.w = 1
goblin_shaman.i = 3
goblin_shaman.a = 1
goblin_shaman.weapon = [
	copy.deepcopy(bosspole)
]

#####
beastmen_hound = Unit()
beastmen_hound.name = "beastmen hound"
beastmen_hound.t = 3
beastmen_hound.s = 4
beastmen_hound.ws = 4
beastmen_hound._as = 0
beastmen_hound.w = 1
beastmen_hound.a = 1
beastmen_hound.i = 4
beastmen_hound.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
beastmen_hound.weapon = [
    copy.deepcopy(yaw)
]

#####
beastmen = Unit()
beastmen.name = "beastmen"
beastmen.t = 4
beastmen.s = 4
beastmen.ws = 4
beastmen._as = 0
beastmen.w = 1
beastmen.a = 1
beastmen.i = 4
# first weapon
beastmen.weapon = [
    copy.deepcopy(club),
    copy.deepcopy(dagger_offhand),
]

beastmen_leader = copy.deepcopy(beastmen)
beastmen_leader.w = 2

#####
mutant = Unit()
mutant.name = "mutant"
mutant.t = 6
mutant.s = 3
mutant.ws = 3
mutant._as = 0
mutant.w = 1
mutant.a = 1
mutant.i = 4
mutant.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
mutant.weapon = [
    copy.deepcopy(two_handed)
]

#####
dwarf1 = Unit()
dwarf1.name = "dwarf 1"
dwarf1.t = 4
dwarf1.s = 3
dwarf1.ws = 3
dwarf1._as = 0
dwarf1.w = 1
dwarf1.a = 1
dwarf1.i = 2
dwarf1.stunnedMax = 5
dwarf1.hardToKill = True
dwarf1.weapon = [
    copy.deepcopy(gromril_axe),
    copy.deepcopy(gromril_axe_offhand)
]
dwarf2 = copy.deepcopy(dwarf1)
dwarf2.name = "dwarf 2"

sig_novice = Unit()
sig_novice.name ="sigmarite novice 1"
sig_novice.ws = 2
sig_novice.s = 3
sig_novice.t = 3
sig_novice.w = 1
sig_novice.i = 1
sig_novice.a = 1
sig_novice.weapon = [
	copy.deepcopy(dagger),
	copy.deepcopy(dagger_offhand)
]

black_ork = Unit()
black_ork.name = "Black ork hired sword"
black_ork.bs = 0
black_ork.ws = 4
black_ork.s = 4
black_ork.t = 5
black_ork.w = 1
black_ork.i = -1 # strike last
black_ork.a = 1
black_ork._as = 3
black_ork.helmet = True
black_ork.weapon = [
	copy.deepcopy(two_handed)
]

vampire_minor = Unit()
vampire_minor.name = "vampire"
vampire_minor.ws = 2
vampire_minor.s = 2
vampire_minor.t = 3
vampire_minor.w = 1
vampire_minor.i = 2
vampire_minor.a = 1
vampire_minor._as = 0
vampire_minor.weapon = [
	copy.deepcopy(yaw)
]

vampire_master = Unit()
vampire_master.name = "Buerghomeister vampire"
vampire_master.bs = 3
vampire_master.rs = 2
vampire_master.ws = 4
vampire_master.s = 4
vampire_master.t = 4
vampire_master.w = 2
vampire_master.i = 5
vampire_master.a = 2
vampire_master._as = 0
vampire_master.skullOfIron = True # stunned as knocked down
vampire_minor.weapon = [
	copy.deepcopy(yaw)
]

initiate = Unit()
initiate.name = "Gaius Cordovan Eslam Galotta"
initiate.ws = 3
initiate.s = 4
initiate.t = 4
initiate.w = 1
initiate.i = 3
initiate.a = 1
initiate._as = 0
initiate.rabbitsFoot = True
initiate.weapon = [
	copy.deepcopy(dagger),
	copy.deepcopy(dagger_offhand)
]

