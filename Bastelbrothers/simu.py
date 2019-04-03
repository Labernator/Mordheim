
import random
import copy

class Prestate:
    w = 0
    state = 0

class Unit:
    name = "troll"
    t = 4
    s = 5
    ws = 3
    _as = 4
    w = 3
    a = 3
    i = 1
    state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
    pre_state = 0 # 0 = normal, 1 = knocked down, 2 = stunned, 3 = ooa
    stunnedMin = 3
    stunnedMax = 4
    causedWounds = 0
    regeneration = False

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
troll = Unit()
troll.regeneration = True

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
grumlok = Unit()
grumlok.name = "grumlok"
grumlok.t  = 4
grumlok.s  = 4
grumlok.w  = 1
grumlok.a  = 2
grumlok.ws = 4
grumlok._as = 4
grumlok.i = 3
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
        "a" : 1,
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
ork_hero2 = copy.deepcopy(ork_hero)
ork_hero2.name = "ork hero 2"
ork_hero3 = copy.deepcopy(ork_hero)
ork_hero3.name = "ork hero 3"

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
beastmen.s = 3
beastmen.ws = 4
beastmen._as = 0
beastmen.w = 1
beastmen.a = 1
beastmen._as = 4
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
        "stunnedMin" : 3,
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
    print "T S WS AS W A I St CW"
    state = ""
    if u.state == 0:
        state = "-"
    elif u.state == 1:
        state = "knd"
    elif u.state == 2:
        state = "stn"
    else:
        state = "ooa"

    out = str(u.t) + " " + str(u.s) + "  " + str(u.ws) + "  " + str(u._as) + " " + str(u.w) + " " + str(u.a) + " " + str(u.i) + " " + state + " "
    if state == "-":
      out = out + " "
    out = out + str(u.causedWounds)
    print out

def attack(u1, u2, wn, first_round = False):

    u2_w_old = u2.w

    # TODO betrachtung der pre states einfuehren
    if u2.state == 0:
        # HIT
        hit_granted = tryToHit(u1, u2, wn)
    else:
        if u2.pre_state == 0:
        	hit_granted = tryToHit(u1, u2, wn)
	else:
        	print "\tauto hit"
        	hit_granted = True # autohit because the target is knocked down   

    if hit_granted == True:
        # WOUND
        wound_granted = tryToWound(u1, u2, wn, first_round)
        if wound_granted == True:

            # ARMOR SAVE
            as_granted = tryArmorSave(u1, u2, wn)

            if as_granted == False:
                print "\t\twound"

                # INJURY
                tryToInjure(u1, u2, wn, u2_w_old)
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
    tmp_s = tmp_s + u1.weapon[wn]["s"]
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

    if u2.regeneration == True:
        print "\t\t\twound regeneration on 4+"
        roll = rollD6()
        print "\t\t\twound regeneration roll: " + str(roll)
        if roll >= 4:
            print "\t\t\tgranted"
            return True
        else:
            print "\t\t\tno wound regeneration"

    return False

def tryToInjure(u1, u2, wn, u2_w_old):
    injury_addition = 0
    if u2.w > 0:
	u1.causedWounds = u1.causedWounds + 1
        u2.w = u2.w - 1;
    if u2_w_old == 0:
        injury_addition = 1
        print "\t\t\tinjury roll +1"

    doInjuryRoll(u1, u2, wn, injury_addition)
    # hier auch die injudies erwurfeln wenn u2.w = 0 ist und der angreifer u1 mehr als eine wunde in dieser runde verursacht hat
    # bedingungen:
    # u2.w == 0
    # u1.attacken > 0
    # u1.wunden ausgeloest > 0
    # anz injury rolls = u1.

def doInjuryRoll(u1, u2, wn, injury_addition):
    if u2.w == 0:
        roll = rollD6() + injury_addition
        print "\t\t\tinjury roll: " + str(roll)
        # TODO stunnedMax und stunnedMin von unit und waffen beachten
        if roll < u1.weapon[wn]["stunnedMin"]:
            print "\t\t\tknocked down"
            if u2.state == 0:
                u2.state = 1
		u2.pre_state = u2.state
        elif roll >= u1.weapon[wn]["stunnedMin"] and roll <= u2.stunnedMax:
            print "\t\t\tstunned"
            if u2.state < 2:
		u2.pre_state = u2.state
                u2.state = 2
        else:
            print "\t\t\tooa"
            if u2.state < 3:
		u2.pre_state = u2.state
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
            print "\n----------"
            printChar(attacker)
            printChar(target)
            print

            print "\t\tauto hit & wound"
            print "\t\tauto ooa\n"

            target.state = 3 # out of action

            printChar(attacker)
            printChar(target)
            print

def allAttackersDead(attackers):
    allAttackersDead = True
    for a in attackers:
        if a.state < 3:
            allAttackersDead = False
            break
    return allAttackersDead

if __name__ == "__main__":

    attackers = []
    #attackers += [ squig, g1, g2 ]

    #attackers += [ sq1, sq2, sq3, sq4, sq5 ]
    #attackers += [ sq1, sq2, sq3, sq4, sq5 ]
    attackers += [ sq1, sq2 ]
    #attackers += [ g1, g2, g3, g4 ]
    #attackers += [ ob1, ob2, ob3 ]
    attackers += [ ork_hero1, ork_hero2, ork_hero3 ]
    attackers += [ ork_shaman ]
    #attackers += [ troll ]
    attackers += [ grumlok ]
    #attackers += [ troll, mutant, pit_ogre, beastmen, ork_shaman, dwarf1, centigor ]
    target = belandysh
    #target = centigor
    #target = pit_ogre
    first_round = True

    rounds = 0

    while allAttackersDead(attackers) == False and target.state < 3:
	if target.name == "belandysh":
            target.ws = random.randint(1,6)
            target.s = random.randint(1,6)
            target.t = random.randint(1,6)
            target.a = random.randint(2,4)
            print "---- Belandysh stats for this round"
            printChar(target)
            print "----"

        if first_round == True:
            # do the charges
            for attacker in attackers:
                if attacker.state == 0:
                    # TODO reihenfolge anhaengig von stunned/knockdown/initiative/strikeFirst/strikeLast
                    doFight(attacker, target, first_round)

            print "---- Belandysh stats for this fight"
            printChar(target)
            print "----"
            foes = []
            for i in range(target.a):
                foes.append(attackers[random.randint(1, len(attackers)-1)])
            # TODO unify the list and sum the attacks for each enemy
            for ff in foes:
                tmp_target = copy.deepcopy(target)
                tmp_target.a = 1
                doFight(tmp_target, ff)

            first_round = False

        else:
            all_fighters = attackers + [ target ]
            fights_ini_ordered = []
            tf_num = 0
            tf_cnt = 0
            # 1. liste fer kampfenden nach ini sortieren
	    fights_ini_ordered = sorted(all_fighters, key=lambda x: x.i, reverse=True)
            # 2. die kampfe ausfuhren
            for f in fights_ini_ordered:
                if f != target:
                    doFight(f, target)
                else:
                    # 3. choose f.A foes if has more than one
                    print "---- Belandysh stats for this fight"
                    printChar(target)
                    print "----"
                    foes = []
                    for i in range(f.a):
                        foes.append(attackers[random.randint(1, len(attackers)-1)])
                    # TODO unify the list and sum the attacks for each enemy
                    for ff in foes:
                        tmp_target = copy.deepcopy(target)
                        tmp_target.a = 1
                        doFight(tmp_target, ff)

        print "========="
        rounds = rounds + 1

    print "\n--------------------"
    print str(rounds) + " rounds done"
    for u in attackers:
        printChar(u)
    printChar(target)
    print


