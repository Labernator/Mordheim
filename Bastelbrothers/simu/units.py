
from simu_unit import *
from weapons import *

#####
black_pegasus = Unit()
black_pegasus.name = "Black pegasus"
black_pegasus.ws = 3
black_pegasus.s = 4
black_pegasus.t = 4
black_pegasus.w = 5
black_pegasus.i = 3
black_pegasus.a = 5
black_pegasus._as = 5
black_pegasus.noStrengthSaveMod = True
black_pegasus.skullOfIron = True
black_pegasus.weapon = [
    copy.deepcopy(yaw)
]

#####
grumm_giant = Unit()
grumm_giant.name = "Grumm the giant"
grumm_giant.hardToKill = True
grumm_giant.grabIt = True
grumm_giant.treeStrike = True
grumm_giant.ws = 3
grumm_giant.s = 7
grumm_giant.t = 6
grumm_giant.w = 6
grumm_giant.i = 3
grumm_giant.a = 1
grumm_giant._as = 0
grumm_giant.weapon = [
    copy.deepcopy(club)
]#####
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
champ_of_chaos.weapon = [
    {
        "type" : "great axe",
        "s" : 2,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : -1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
    }
]

#### chaos dragon
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

