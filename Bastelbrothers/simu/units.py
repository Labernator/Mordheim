
from simu_unit import *

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

