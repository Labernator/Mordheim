import copy

club = {
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
}

club_offhand = copy.deepcopy(club)
club_offhand["offhand"] = True

fist = {
        "type" : "fist",
        "s" : -1,
        "firstRoundSAdd" : 0,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "toInjuryRoll" : 0,
        "as" : 1,
        "a" : 0,
        "stunnedMin" : 3,
        "stunnedMax" : 4,
        "range" : False,
}

foot= {
    "type" : "foot",
    "s" : 0,
    "firstRoundSAdd" : 0,
    "offhand" : True,
    "toHitOffhand" : 2, # no hit penality for feet attack
    "toHit" : 0,
    "as" : 0,
    "a" : 0,
    "stunnedMin" : 3,
    "stunnedMax" : 4,
    "range" : False,
}

dagger = {
    "type" : "dagger",
    "s" : 0,
    "firstRoundSAdd" : 0,
    "offhand" : False,
    "toHitOffhand" : 0,
    "toHit" : 0,
    "as" : 1,
    "a" : 0,
    "stunnedMin" : 3,
    "stunnedMax" : 4,
    "range" : False,
}

dagger_offhand = copy.deepcopy(dagger)
dagger_offhand["offhand"] = True
dagger_offhand["toHitOffhand"] = 1

hand_weapon = {
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
}

hand_weapon_offhand = copy.deepcopy(hand_weapon)
hand_weapon_offhand["offhand"] = True

animal_attack = {
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

axe = {
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
}

axe_offhand = copy.deepcopy(axe)
axe_offhand["offhand"] = True

sword = {
    "type" : "sword",
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

sword_offhand = copy.deepcopy(sword)
sword_offhand["offhand"] = True

clubba = {
    "type" : "clubba",
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
}

yaw = {
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

dark_steel_halberd = {
    "type" : "dark steel halberd",
    "s" : 1,
    "firstRoundSAdd" : 0,
    "offhand" : False,
    "toHitOffhand" : 0,
    "toHit" : 0,
    "as" : 0,
    "a" : 0,
    "stunnedMin" : 2,
    "stunnedMax" : 4,
    "range" : False,
}

two_handed = {
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

gromril_axe = {
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
}

gromril_axe_offhand = copy.deepcopy(gromril_axe)
gromril_axe_offhand["offhand"] = True

spear = {
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

bosspole = {
    "type" : "boss pole (spear)",
    "s" : 0,
    "firstRoundSAdd" : 1,
    "offhand" : False,
    "toHitOffhand" : 0,
    "toHit" : 0,
    "toInjuryRoll" : 0, # spider poison +1
    "as" : 0,
    "a" : 0,
    "stunnedMin" : 3,
    "stunnedMax" : 4,
    "range" : False,
}

giantic_spider_yaw = {
    "type" : "venomous spider yaw",
    "s" : 0,
    "firstRoundSAdd" : 0,
    "offhand" : False,
    "toHitOffhand" : 0,
    "toHit" : 0,
    "toInjuryRoll" : 0, # spider poison +1
    "as" : 0,
    "a" : 0,
    "stunnedMin" : 2,
    "stunnedMax" : 4,
    "range" : False,
}

giant_spider_yaw = {
    "type" : "spider yaw",
    "s" : 0,
    "firstRoundSAdd" : 0,
    "offhand" : False,
    "toHitOffhand" : 0,
    "toHit" : 0,
    "toInjuryRoll" : 0, # spider poison +1
    "as" : 0,
    "a" : 0,
    "stunnedMin" : 2,
    "stunnedMax" : 4,
    "range" : False,
}

