
import copy

class Unit:
    name = "troll"
    t = 4
    s = 5
    ws = 3
    _as = 4
    w = 3
    a = 3
    i = 1
    i_orig = 0
    state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
    pre_state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
    stunnedMin = 3
    stunnedMax = 4
    causedWounds = 0
    causedOOA = 0
    firstRoundToHitAdd = 0
    hardToKill = False
    toHitAdd = 0
    regeneration = False
    ardEad = False
    helmet = False
    stepaside = False
    resilient = False
    mightyblow = False
    striketoinjure = False
    hate = False
    hateEverytime = False
    parry = False
    parryImproved = False
    parry_used_this_fight = False
    cantBeAttacked = False
    inconsistency = False
    doNotUseOffhand = False
    luckyCharm = False
    luckyCharmUsed = False

    weapon = [
        {
            "type" : "hand",
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
            "critTable" : 1 # 0 missile, 1 bludge, 2 bladed, 3 unarmed, 4 thrusting
        }
    ]

