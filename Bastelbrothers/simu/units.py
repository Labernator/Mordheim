
from simu_unit import *

#####
troll = Unit()
troll.regeneration = False

#####
centigor = Unit()
centigor.name = "centigor"
centigor.t = 4
centigor.s = 4
centigor.w = 1
centigor.a = 2
centigor.ws = 4
centigor._as = 0
centigor.i = 2
centigor.weapon = [
    {
        "type" : "club",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "club",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "foot",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#####
pit_ogre = Unit()
pit_ogre.name = "pit fighter ogre"
pit_ogre.t  = 4
pit_ogre.s  = 4
pit_ogre.w  = 3
pit_ogre.a  = 2
pit_ogre.ws = 3
pit_ogre._as = 5
pit_ogre.i = 3
pit_ogre.weapon = [
    {
        "type" : "flail",
        "s" : 0,
        "firstRoundSAdd" : 2,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

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
    {
        "type" : "animal attack",
        "s" : 0,
        "firstRoundSAdd" : 2,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }

]

#####
grumlok = Unit()
grumlok.name = "grumlok"
grumlok.t  = 4
grumlok.s  = 4
grumlok.w  = 1
grumlok.a  = 2
grumlok.ws = 4
grumlok._as = 4
grumlok.i = 3
grumlok.helmet = True
grumlok.weapon = [
    {
        "type" : "axe",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : -1,
        "a" : 0,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#####
ork_shaman = Unit()
ork_shaman.name = "wogga"
ork_shaman.t  = 4
ork_shaman.s  = 3
ork_shaman.w  = 1
ork_shaman.a  = 1
ork_shaman.ws = 4
ork_shaman._as = 0
ork_shaman.i = 3
ork_shaman.weapon = [
    {
        "type" : "clubbba",
        "s" : 2,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 1,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#####
ork_hero = Unit()
ork_hero.name = "ork hero"
ork_hero.t  = 4
ork_hero.s  = 3
ork_hero.w  = 1
ork_hero.a  = 1
ork_hero.ws = 4
ork_hero.i = 3
ork_hero.weapon = [
    {
        "type" : "hand weapon",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]
ork_hero1 = copy.deepcopy(ork_hero)
ork_hero1.name = "ork hero 1"
ork_hero1.ws = 5
ork_hero2 = copy.deepcopy(ork_hero)
ork_hero2.name = "ork hero 2"
ork_hero2.s = 4
ork_hero3 = copy.deepcopy(ork_hero)
ork_hero3.name = "ork hero 3"
ork_hero3.t = 3

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
    {
        "type" : "yaw",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
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
    {
        "type" : "yaw",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
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
beastmen._as = 4
beastmen.i = 3
beastmen.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
beastmen.weapon = [
    {
        "type" : "club",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "club",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 2,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#####
belandysh = Unit()
belandysh.name = "belandysh"
belandysh.t = 6
belandysh.s = 6
belandysh.ws = 6
belandysh._as = 2
belandysh.w = 3
belandysh.a = 4
belandysh.i = 6
belandysh.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
belandysh.regeneration = True
belandysh.helmet = True
belandysh.inconsistency = True
# first weapon
belandysh.weapon = [
    {
        "type" : "two-handed",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]


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
    {
        "type" : "two-handed",
        "s" : 2,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#####
champ_of_chaos = Unit()
champ_of_chaos.name = "Champion of Chaos"
champ_of_chaos.ws = 7
champ_of_chaos.s = 5
champ_of_chaos.t = 4
champ_of_chaos.w = 2
champ_of_chaos.i = 6
champ_of_chaos.a = 4
champ_of_chaos._as = 3
champ_of_chaos.stepaside = True
champ_of_chaos.helmet = True
champ_of_chaos.mightyblow = True
champ_of_chaos.weapon[0]["type"] = "great axe"
champ_of_chaos.weapon[0]["s"] = 2
champ_of_chaos.weapon[0]["as"] = -1

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
dwarf1.weapon = [
    {
        "type" : "gromril axe",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : -2,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "gromril axe",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : -2,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]
dwarf2 = copy.deepcopy(dwarf1)
dwarf2.name = "dwarf 2"

#####
ob1 = Unit()
ob1.name = "ork boy 1"
ob1.t = 4
ob1.s = 3
ob1.ws = 3
ob1._as = 0
ob1.w = 1
ob1.a = 1
ob1.i = 2
ob1.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
ob1.weapon = [
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
    ,
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]
####
ob2 = copy.deepcopy(ob1)
ob2.name = "ork boy 2"
####
ob3 = copy.deepcopy(ob1)
ob3.name = "ork boy 3"
####
ob4 = copy.deepcopy(ob1)
ob4.i = 3
ob4.name = "ork boy 4"
####
ob5 = copy.deepcopy(ob1)
ob5.i = 3
ob5.name = "ork boy 5"

####
g1 = Unit()
g1.name = "goblin 1"
g1.t = 3
g1.s = 3
g1.ws = 2
g1._as = 0
g1.w = 1
g1.a = 1
g1.i = 4
g1.state = 0
g1.weapon = copy.deepcopy(ob1.weapon)
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
    {
        "type" : "spear",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

chaos_warr = Unit()
chaos_warr.name = "Chaos warrior"
chaos_warr.ws=6
chaos_warr.s=4
chaos_warr.t=4
chaos_warr.w=1
chaos_warr.i=6
#chaos_warr.a=2
chaos_warr.a=3 # frenzy + 4+ magic save
chaos_warr._as=4 # heavy armor
chaos_warr.helmet=True
chaos_warr.parry=False # sword only
chaos_warr.weapon = [
    {
        "type" : "axe",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : -1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    },
    {
        "type" : "axe",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : -1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

chaos_dragon = Unit()
chaos_dragon.name = "Chaos dragon"
chaos_dragon.ws=6
chaos_dragon.s=6
chaos_dragon.t=6
chaos_dragon.w=6
chaos_dragon.i=3
chaos_dragon.a=6
chaos_dragon._as=3
chaos_dragon.helmet=False
chaos_dragon.parry=False # sword only
chaos_dragon.weapon = [
    {
        "type" : "claws",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

