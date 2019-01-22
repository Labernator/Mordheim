
import random

class Unit:
    name = "troll"
    t = 4
    s = 5
    ws = 3
    _as = 4
    w = 3
    a = 3
    state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa

    weapon = [
        {
            "type" : "hand",
            "s" : 0,
            "firstRoundSAdd" : 2,
            "offhand" : False,
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
beastmen = Unit()
beastmen.name = "beastmen"
beastmen.t = 4
beastmen.s = 3
beastmen.ws = 4
beastmen._as = 0
beastmen.w = 2
beastmen.a = 1
beastmen.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# first weapon
beastmen.weapon = [
    {
        "type" : "flail",
        "s" : 0,
        "firstRoundSAdd" : 2,
        "offhand" : False,
        "toHitOffhand" : 0,
        "toHit" : 0,
        "as" : 0,
        "a" : 0,
        "range" : False,
    }
]
###
mutant = Unit()
mutant.name = "mutant"
mutant.t = 6
mutant.s = 3
mutant.ws = 3
mutant._as = 0
mutant.w = 1
mutant.a = 1
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
        "range" : False,
    }
]

#####
ob1 = Unit()
ob1.name = "ork boy 1"
ob1.t = 4
ob1.s = 3
ob1.ws = 3
ob1._as = 0
ob1.w = 1
ob1.a = 1
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
        "range" : False,
    }
]
###
ob2 = Unit()
ob2.name = "ork boy 2"
ob2.t = 4
ob2.s = 3
ob2.ws = 3
ob2._as = 0
ob2.w = 1
ob2.a = 1
ob2.state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
# the weapon
ob2.weapon = [
    {
        "type" : "dagger",
        "s" : 0,
        "firstRoundSAdd" : 0,
        "offhand" : True,
        "toHitOffhand" : 1,
        "toHit" : 0,
        "as" : 1,
        "a" : 0,
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
        "range" : False,
    }
]

def rollD6():
    return random.randint(1,6)

def getMinHitRoll(ws1, ws2):
    if ws1 > ws2:
        return 3
    else:
        return 4

def getMinWoundRoll(s, t):
    if s >= t+2:
        r = 2
    elif s == t+1:
        r = 3
    elif s == t:
        r = 4
    elif s == t-1:
        r = 5
    else:
        r = 6
    #print "r = " + str(r)
    return r

def printChar(u):
    print u.name + " characteristics"
    print "T S WS AS W A St"
    state = ""
    if u.state == 0:
        state = "-"
    elif u.state == 1:
        state = "knd"
    elif u.state == 2:
        state = "stn"
    else:
        state = "ooa"

    print str(u.t) + " " + str(u.s) + "  " + str(u.ws) + "  " + str(u._as) + " " + str(u.w) + " " + str(u.a) + " " + state

def attack(u1, u2, wn, first_round = False):

    u2_w_old = u2.w

    # HIT
    hit_granted = tryToHit(u1, u2, wn)
    if hit_granted == True:

        # WOUND
        wound_granted = tryToWound(u1, u2, wn, first_round)
        if wound_granted == True:

            # ARMOR SAVE
            as_granted = tryArmorSave(u1, u2, wn)

            if as_granted == False:
                print "\t\twound"

                # INJURY
                tryToInjure(u1, u2, u2_w_old)
            else:
                print "\t\tno wound"

def tryToHit(u1, u2, wn):

    minHitRoll = getMinHitRoll(u1.ws, u2.ws)
    roll = rollD6()
    if u1.weapon[wn]["offhand"] == True:
        if u1.weapon[wn]["toHitOffhand"] != 0:
            print "\toffhand to hit mod " + str(u1.weapon[wn]["toHitOffhand"])
            minHitRoll = minHitRoll + 2 + (u1.weapon[wn]["toHitOffhand"] * -1)
        else:
            print "\toffhand -2 to hit"
            minHitRoll = minHitRoll + 2
    if u1.weapon[wn]["toHit"] != 0:
        print "\tto hit mod " + str(u1.weapon[wn]["toHit"])
        minHitRoll = minHitRoll + (u1.weapon[wn]["toHit"] * -1)

    print "\tto hit on " + str(minHitRoll)
    print "\tHit roll: " + str(roll)

    if roll >= minHitRoll:
        print "\thit"
        return True

    return False

def tryToWound(u1, u2, wn, first_round = False):
    tmp_s = 0
    if first_round == True:
        tmp_s = u1.weapon[wn]["firstRoundSAdd"]
    minWoundRoll = getMinWoundRoll(u1.s + tmp_s, u2.t)
    roll = rollD6()

    print "\t\tto wound on " + str(minWoundRoll)
    print "\t\twound roll: " + str(roll)

    if roll >= minWoundRoll:
        if roll == 6 and minWoundRoll < 6:
            roll = rollD6()
            print "\t\tcrit: " + str(roll)
        return True

    return False

def tryArmorSave(u1, u2, wn):
    t_as = u2._as

    if t_as == 0:
        t_as = 7

    if u1.s > 3:
        print "\t\t\tS" + str(u1.s) + " -" + str(u1.s - 3) + "AS"
        t_as = t_as + (u1.s - 3)

    if u1.weapon[wn]["s"] > 0:
        print "\t\t\tweapon S" + str(u1.weapon[wn]["s"]) + " " + str(u1.weapon[wn]["s"] * -1) + "AS"
        t_as = t_as + u1.weapon[wn]["s"]

    if u1.weapon[wn]["as"] != 0:
        print "\t\t\tweapon as mod " + str(u1.weapon[wn]["as"]) + "AS"
        t_as = t_as + (u1.weapon[wn]["as"] * -1)

    print "\t\t\tarmor save on " + str(t_as)

    if t_as < 7:
        roll = rollD6()
        print "\t\t\tarmor save roll: " + str(roll)
    else:
        roll = 0

    if roll >= t_as:
        print "\t\t\tgranted"
        return True
    else:
        print "\t\t\tno armor save"

    return False

def tryToInjure(u1, u2, u2_w_old):
    injury_addition = 0
    if u2.w > 0:
        u2.w = u2.w - 1;
    if u2_w_old == 0:
        injury_addition = 1
        print "\t\t\tinjury roll +1"

    doInjuryRoll(u2, injury_addition)
    # hier auch die injudies erwurfeln wenn u2.w = 0 ist und der angreifer u1 mehr als eine wunde in dieser runde verursacht hat
    # bedingungen:
    # u2.w == 0
    # u1.attacken > 0
    # u1.wunden ausgeloest > 0
    # anz injury rolls = u1.

def doInjuryRoll(u2, injury_addition):
    if u2.w == 0:
        roll = rollD6() + injury_addition
        print "\t\t\tinjury roll: " + str(roll)
        if roll < 3:
            print "\t\t\tknocked down"
            if u2.state == 0:
                u2.state = 1
        elif roll > 2 and roll < 5:
            print "\t\t\tstunned"
            if u2.state < 2:
                u2.state = 2
        else:
            print "\t\t\tooa"
            if u2.state < 3:
                u2.state = 3

def doAllAttacks(u1, u2, first_round = False):
    a_main = u1.a
    a_off = 0
    off_weapon = -1
    main_weapon = -1

    print "\n----------"
    printChar(u1)
    printChar(u2)
    print

    i = 0
    for w in u1.weapon:
        if w['range'] != True:
            if w["offhand"] == True:
                if w["a"] != 0:
                    a_off = a_off + w["a"]
                off_weapon = i
            elif w['offhand'] == False:
                if w["a"] != 0:
                    a_main = a_main + w["a"]
                main_weapon = i
        i = i + 1

    if main_weapon > -1:
        for w in range(0, a_main):
            attack(u1, u2, main_weapon, first_round) # do the w'th attack
            print

    if off_weapon > -1:
        a_off = a_off + 1
        for w in range(0, a_off):
            attack(u1, u2, off_weapon, first_round) # do the w'th attack
            print

    printChar(u1)
    printChar(u2)
    print

def doFight(attacker, target, first_round = False):
        if target.state == 0:
            doAllAttacks(attacker, target, first_round)
        elif target.state == 1: # knocked down
            doAllAttacks(attacker, target)
        elif target.state == 2:
            target.state = 3 # out of action
            print "\t\tauto hit & wound"
            print "\t\tauto ooa"

if __name__ == "__main__":

    attackers = [ ob1, ob2 ]
    target = mutant
    first_round = True

    rounds = 0
    while not (attackers[0].state == 3 or attackers[1].state == 3) and target.state < 3:
        for attacker in attackers:
            if attacker.state == 0:
                # TODO reihenfolge anhaengig von stunned/knockdown/initiative/strikeFirst/strikeLast
                doFight(attacker, target, first_round)

        if target.state == 0:
            # strike back
            for attacker in attackers:
                if attacker.state < 3:
                    doAllAttacks(target, attacker)
                    break # all defined attacks only one time

        first_round = False

        print "========="
        rounds = rounds + 1

    print "\n----------"
    print str(rounds) + " rounds done"
    printChar(ob1)
    printChar(ob2)
    printChar(target)
    print


