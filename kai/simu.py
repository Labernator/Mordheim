
import random

class unit_2:
    name = "troll"
    t = 3
    s = 5
    ws = 3
    _as = 4
    w = 3
    a = 3
    state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa

    weapon = [
        {
            "type" : "club",
            "s" : 0,
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

class unit_1:
    name = "rat"
    t = 3
    s = 3
    ws = 3
    _as = 0
    w = 1
    a = 1
    state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa

    # the first weapon
    weapon = [
        {
            "type" : "dagger",
            "s" : 0,
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

def attack(u1, u2, wn):

    u2_w_old = u2.w

    # HIT
    hit_granted = tryToHit(u1, u2, wn)
    if hit_granted == True:

        # WOUND
        wound_granted = tryToWound(u1, u2)
        if wound_granted == True:

            # ARMOD SAVE
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

def tryToWound(u1, u2):
    minWoundRoll = getMinWoundRoll(u1.s, u2.t)
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
        t_as = 6

    if u1.s > 3:
        print "\t\t\tS" + str(u1.s) + " -" + str(u1.s - 3) + "AS"
        t_as = t_as + (u1.s - 3)

    if u1.weapon[wn]["s"] > 0:
        print "\t\t\tweapon S" + str(u1.weapon[wn]["s"]) + " " + str(u1_weapon[wn]["s"] * -1) + "AS"
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

def doAllAttacks(u1, u2):
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
            attack(u1, u2, main_weapon) # do the w'th attack
            print

    if off_weapon > -1:
        a_off = a_off + 1
        for w in range(0, a_off):
            attack(u1, u2, off_weapon) # do the w'th attack
            print

    printChar(u1)
    printChar(u2)
    print

if __name__ == "__main__":

    doAllAttacks(unit_2, unit_1)
    if unit_1.state == 0:
        doAllAttacks(unit_1, unit_2)
    elif unit_1.state == 1: # knocked down
        unit_1.state = 0
        doAllAttacks(unit_2, unit_1) # strike last for the unit_1
    elif unit_1.state == 2:
        unit_1.state = 1

        print "\n----------"
        print
        printChar(unit_1)
        printChar(unit_2)
        print

        if tryToWound(unit_2, unit_1):
            unit_1.state = 3 # out of action
            print "\t\tauto hit & wound"
            print "\t\tauto ooa"

