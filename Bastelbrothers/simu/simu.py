
import sys, os

from deco import *

import random
import copy

from simu_unit import *

#from fight_declaration_kai import * # enable to debug only

try:
  from fight_declaration_kai import *
except:
  from fight_declaration import *

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-m", "--maxtries", dest="max_tries",
                    help="maximum tries", default=1, type=int)
parser.add_argument("-q", "--quiet",
                    dest="quiet", default=False, action='store_true',
                    help="don't print status messages to stdout")

crit_table = [
    [ # missile
      [ { "as" : 0 }, { "as" : 0 }, { }, { }, { "wounds" : 2 }, { "wounds" : 2 } ]
    ],
    [ # bludge
    ],
    [ # blade
    ],
    [ # unarmed
    ],
    [ # thrusting
    ],
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
    print "WS S T W I A AS St  CW CooA"
    state = ""
    if u.state == 0:
        state = "-"
    elif u.state == 1:
        state = "knd"
    elif u.state == 2:
        state = "stn"
    else:
        state = "ooa"

    out = str(u.ws) + "  " + str(u.s) + " " + str(u.t) + " " + str(u.w) + " " + str(u.i) + " " + str(u.a) + " " + str(u._as)
    if u.i > 0:
      out = out + "  "
    else:
      out = out + " "
    out = out + state + " "

    if state == "-":
      out = out + "  "

    out = out + str(u.causedWounds)

    out = out + "  " + str(u.causedOOA)

    print out

def attack(u1, u2, wn, first_round = False):

    u2_w_old = u2.w
    if u1.weapon[wn]["offhand"] == True:
        print "\toff hand (" + u1.weapon[wn]["type"] + "):"
    else:
        print "\tmain hand (" + u1.weapon[wn]["type"] + "):"

    if u2.state == 0:
        # try to hit
        hit_granted = tryToHit(u1, u2, wn, first_round)
    else: # u2 is not in state normal
        if u2.pre_state == 0:
                # try to hit the target because it was not > normal in the last round
                hit_granted = tryToHit(u1, u2, wn, first_round)
        else:
                # autohit because the target is knocked down
                print "\tauto hit"
                hit_granted = True

    if hit_granted == True:
        # WOUND
        wound_granted = tryToWound(u1, u2, wn, first_round)

        if wound_granted == True:
            if u2.pre_state == 1 and wound_granted == True:
                # we have caused a wound and in the previois state the enemy was already knocked down
                u2.w = 0
                u2.state = 3
                print "\t\twound & ooa"
                return True

            # ARMOR SAVE
            as_granted = tryArmorSave(u1, u2, wn)

            if as_granted == False:
                print "\t\twound"

                # INJURY
                tryToInjure(u1, u2, wn, u2_w_old)
            else:
                print "\t\tno wound"

def tryToHit(u1, u2, wn, first_round = False):

    minHitRoll = getMinHitRoll(u1.ws, u2.ws)
    roll = rollD6()

    if first_round == True and u1.firstRoundToHitAdd > 0:
        print "\t" + u1.name + " has +" + str(u1.firstRoundToHitAdd) + " to hit in the first round"
        roll = roll + u1.firstRoundToHitAdd

    if u1.toHitAdd > 0:
        print "\t" + u1.name + " has +" + str(u1.toHitAdd) + " to hit"
        roll = roll + u1.toHitAdd

    if u1.weapon[wn]["offhand"] == True:
        if u1.weapon[wn]["toHitOffhand"] != 0:
            print "\tto hit addition " + str(u1.weapon[wn]["toHitOffhand"])
            minHitRoll = minHitRoll + 2 + (u1.weapon[wn]["toHitOffhand"] * -1)
        else:
            print "\toff hand -2 to hit"
            minHitRoll = minHitRoll + 2

    if u1.weapon[wn]["toHit"] != 0:
        print "\tto hit mod " + str(u1.weapon[wn]["toHit"])
        minHitRoll = minHitRoll + (u1.weapon[wn]["toHit"] * -1)

    print "\tto hit on " + str(minHitRoll)
    print "\thit roll: " + str(roll)

    if roll < minHitRoll:
      # no hit
      if u1.hate == True or u1.hateEverytime == True:
        print "\t" + u1.name + " hates " + u2.name + ", re-roll"
        roll = rollD6()
        print "\tnew hit roll: " + str(roll)

    if roll >= minHitRoll:
        print "\thit"

        if u2.luckyCharm == True and u2.luckyCharmUsed == False:
            # lucky charm
            u2.luckyCharmUsed = True
            lcRoll = rollD6()
            print "\t" + u2.name + " wear a lucky charm (4+ hit save)"
            print "\troll: " + str(lcRoll)
            if lcRoll >= 4:
                if lcRoll == 6:
                    print "\tthe lucky charm is broken because the roll was a 6"
                    u2.luckyCharm = False
                print "\tno hit"
                return False # no hit

        if roll < 6 and u2.parry == True and u2.parry_used_this_fight == False:
            # parry
            u2.parry_used_this_fight = True

            tmp_parryMin = roll + 1

            if u2.parryImproved == True:
                tmp_parryMin = roll

            print "\tparry on " + str(tmp_parryMin) + "+"

            roll = rollD6()
            print "\tparry roll " + str(roll)

            if roll >= tmp_parryMin:
                print "\tparried"
                return False

            else:
                print "\tno parry"

        return True

    print "\tno hit"

    return False

def tryToWound(u1, u2, wn, first_round = False):
    tmp_s = 0

    if first_round == True:
       if u1.weapon[wn]["firstRoundSAdd"] > 0:
        print "\t\tfirst round +" + str(u1.weapon[wn]["firstRoundSAdd"]) + "S"
        tmp_s = u1.weapon[wn]["firstRoundSAdd"]

    if u1.weapon[wn]["s"] > 0:
        print "\t\tweapon " + u1.weapon[wn]["type"]  + " +" + str(u1.weapon[wn]["s"]) + "S"
        tmp_s = tmp_s + u1.weapon[wn]["s"]

    minWoundRoll = getMinWoundRoll(u1.s + tmp_s, u2.t)
    roll = rollD6()
    print "\t\twound roll: " + str(roll)

    if u1.mightyblow == True:
        print "\t\t" + u1.name + " has skill \"mighty blow\":\n\t\t\t +1 to wound roll"
        roll = roll + 1
        print "\t\tnew wound roll: " + str(roll)

    if u2.resilient == True:
        print "\t\t" + u2.name + " has skill \"resilient\":\n\t\t\t-1 to wound roll"
        roll = roll - 1
        print "\t\tnew wound roll: " + str(roll)

    print "\t\tto wound on " + str(minWoundRoll)

    if roll >= minWoundRoll:
        if roll == 6 and minWoundRoll < 6 and u1.mightyblow == False:
            roll = rollD6()
            print "\t\tcrit: " + str(roll)
        return True

    print "\t\tno wound"
    return False

def tryArmorSave(u1, u2, wn):
    t_as = u2._as

    if t_as == 0:
        t_as = 7

    if u1.s > 3 and u2.noStrengthSaveMod == False:
        print "\t\t\tS" + str(u1.s) + " = -" + str(u1.s - 3) + "AS"
        t_as = t_as + (u1.s - 3)

    if u1.weapon[wn]["s"] > 0 and u2.noStrengthSaveMod == False:
        print "\t\t\tweapon +" + str(u1.weapon[wn]["s"]) + "S " + str(u1.weapon[wn]["s"] * -1) + "AS"
        t_as = t_as + u1.weapon[wn]["s"]

    if u2.noStrengthSaveMod == True:
        print "\t\t\t" + u2.name + " has skill \"save\":\n\t\t\t\tno strength save mod is allowed"

    if u1.weapon[wn]["as"] != 0:
        tmp_as_mod_str = ""
        if u1.weapon[wn]["as"] > 0:
            tmp_as_mod_str = "+"

        tmp_as_mod_str = tmp_as_mod_str + str(u1.weapon[wn]["as"])

        print "\t\t\tweapon as mod " + tmp_as_mod_str
        t_as = t_as + (u1.weapon[wn]["as"] * -1)

    print "\t\t\tarmor save on " + str(t_as)

    if t_as < 7:
        roll = rollD6()
        print "\t\t\tarmor save roll: " + str(roll)
    else:
        roll = 0

    if roll >= t_as:
        print "\t\t\tas granted"
        return True
    else:
        print "\t\t\tno armor save"

    if u2.stepaside == True:
        print "\t\t\tstep aside on 5+"
        roll = rollD6()
        print "\t\t\tstep aside roll: " + str(roll)
        if roll >= 5:
            print "\t\t\tstepped aside"
            return True
        else:
            print "\t\t\tno step aside"

    if u2.regeneration == True:
        print "\t\t\twound regeneration on 4+"
        roll = rollD6()
        print "\t\t\twound regeneration roll: " + str(roll)
        if roll >= 4:
            print "\t\t\twound regenerated"
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
        if injury_addition > 0:
            roll = roll + injury_addition
            print "\t\t\tnew injury roll: " + str(roll)

        if u1.striketoinjure == True:
            print "\t\t\t" + u1.name + " has skill \"strike to injure\":\n\t\t\t\t +1 to injury roll"
            roll = roll + 1
            print "\t\t\tnew injury roll: " + str(roll)

        if "toInjuryRoll" in u1.weapon[wn] and u1.weapon[wn]["toInjuryRoll"] > 0:
            print "\t\t\t" + u1.name + " has +" + str(u1.weapon[wn]["toInjuryRoll"]) + " on injury roll on weapon " + u1.weapon[wn]["type"] + " (" + str(wn) + ")"
            roll = roll + u1.weapon[wn]["toInjuryRoll"]
            print "\t\t\tnew injury roll: " + str(roll)

        if u2.hardToKill == True:
            print "\t\t\t" + u2.name + " has skill \"hard to kill\""

        # stunnedMax und stunnedMin von unit und waffen beachten
        if (roll < u1.weapon[wn]["stunnedMin"] and u2.hardToKill == False) or \
           (u2.hardToKill == True and roll < 3):
            print "\t\t\tknocked down"

            if u2.state == 0:
                u2.state = 1
                u2.i_orig = u2.i
                u2.i = -9 # strike last

        elif (roll >= u1.weapon[wn]["stunnedMin"] and roll <= u2.stunnedMax and u2.hardToKill == False) or \
             (u2.hardToKill == True and roll >=3 and roll <= 5):
            tmp_stnSv = 4
            if u2.helmet == True:
                print "\t\t\tHelmet: stunned save on " + str(tmp_stnSv) + "+"

            if u2.ardEad == True and u2.helmet == False:
                tmp_stnSv = 3
                print "\t\t\tOrk ard ead: stunned save on " + str(tmp_stnSv) + "+"

            if u2.ardEad == True and u2.helmet == True:
                tmp_stnSv = 2; # ard ead increases helmet save by 1
                print "\t\t\tOrk ard ead combined with helmet: stunned save on " + str(tmp_stnSv) + "+"

            if u2.ardEad == True or u2.helmet == True:
                roll = rollD6()

                print "\t\t\tstunned save roll: " + str(roll)
                if roll >= tmp_stnSv:
                    print "\t\t\tgranted, knocked down instead"
                    u2.state = 1
                    u2.i_orig = u2.i
                    u2.i = -9 # strike last
                    return True

            print "\t\t\tstunned"

            if u2.state < 2: # if not also ooA at the same time
                if u2.skullOfIron == True:
                   print "\t\t\t" + u2.name + " has skill \"skull of iron\":\n\t\t\t\tmodifies stunned result into knocked down"
                   u2.state = 1 # knock down instead of stunned
                else:
                    u2.state = 2 # stunned
                    
                u2.i_orig = u2.i
                u2.i = -9 # strike last
        else:
            print "\t\t\tooa"

            if u2.state < 3:
                u2.state = 3
                u1.causedOOA = u1.causedOOA + 1


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

    # TODO if there are more than two weapon set only the last off hand weapon in the list will be used to process the off hand attacks
    if main_weapon > -1:
        for w in range(0, a_main):
            attack(u1, u2, main_weapon, first_round) # do the w'th attack
            print
            if u2.state == 3: # ooa
                break

    if u2.state < 3 and off_weapon > -1 and u1.doNotUseOffhand == False:
        a_off = a_off + 1
        for w in range(0, a_off):
            attack(u1, u2, off_weapon, first_round) # do the w'th attack
            print

    u2.parry_used_this_fight = False # reset the parry used flag
    u1.hate = False # hate is only allowed for one round
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
            attacker.causedOOA = attacker.causedOOA + 1

            printChar(attacker)
            printChar(target)
            print

def allAttackersDead(attackers):
    allAttackersDead = True
    for a in attackers:
        if a.state < 3 and a.cantBeAttacked == False:
            allAttackersDead = False
            break

    return allAttackersDead

def getStrState(s):
    if s == 0:
        return "normal"
    if s == 1:
        return "knd"
    if s == 2:
        return "stn"
    if s == 3:
        return "ooa"

@concurrent
def fightTilOOA(fighters):

    tmp_att = fighters[0]
    tmp_tgt = fighters[1]

    first_round = True

    all_fighters = tmp_att + [ tmp_tgt ]

    rounds = 0

    while allAttackersDead(tmp_att) == False and tmp_tgt.state < 3:

        if tmp_tgt.inconsistency == True:
            tmp_tgt.ws = random.randint(1,6)
            tmp_tgt.s = random.randint(1,6)
            tmp_tgt.t = random.randint(1,6)
            tmp_tgt.a = random.randint(2,4)
            if tmp_tgt.i > 0:
                tmp_tgt.i = random.randint(1,6)

            #enablePrint()
            print "\n---- " + tmp_tgt.name + " stats for this round"
            printChar(tmp_tgt)
            print "---"
            #if args.quiet == True:
            #    blockPrint()

        for a in tmp_att:
            if a.inconsistency == True:
                a.ws = random.randint(1,6)
                a.s = random.randint(1,6)
                a.t = random.randint(1,6)
                a.a = random.randint(2,4)
                if a.i > 0:
                    a.i = random.randint(1,6)

                print "\n---- " + tmp_tgt.name + " stats for this round"
                printChar(a)
                print "---"

        if first_round == True:
            # do the charges
            for attacker in tmp_att:
                if attacker.state == 0:
                    tmp_tgt.pre_state = tmp_tgt.state
                    doFight(attacker, tmp_tgt, first_round)

            #target.state = 3
            if tmp_tgt.state == 0:

                print "---- " + tmp_tgt.name + " (" + getStrState(tmp_tgt.state) + "): selected foes to attack (" + str(tmp_tgt.a) + "A possible)"
                foes = []
                tmp_doNotUseOffhand = False
                for i in range(tmp_tgt.a):

                    # select targets for the attacks
                    j = random.randint(0, len(tmp_att)-1)
                    while tmp_att[j].state > 0 or tmp_att[j].cantBeAttacked == True:
                        j = random.randint(0, len(tmp_att)-1)

                    print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state)

                    tmp_inc = False # increase the number of attacks against the choosen atackers[j]
                    for k in range(len(foes)):
                        if foes[k][0] == tmp_att[j]:
                            if tmp_doNotUseOffhand == False:
                                foes[k][0].doNotUseOffhand = True if random.randint(0,1) else False
                                tmp_doNotUseOffhand = True
                                if tmp_tgt.weapon[0]["offhand"] == True or \
                                   (len(tmp_tgt.weapon) > 1 and \
                                    tmp_tgt.weapon[1]["offhand"] == True):

                                  print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state) + " off hand attack"

                            foes[k][1] = foes[k][1] + 1
                            tmp_inc = True
                            break

                    if tmp_inc == False: # the attacker is not part of the list which defines the number of attacks
                        foes.append([tmp_att[j], 1])
                        if tmp_doNotUseOffhand == False:
                            foes[-1][0].doNotUseOffhand = True if random.randint(0,1) else False
                            tmp_doNotUseOffhand = True
                            if tmp_tgt.weapon[0]["offhand"] == True or \
                               (len(tmp_tgt.weapon) > 1 and \
                                tmp_tgt.weapon[1]["offhand"] == True):

                              print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state) + " off hand attack"

                for ff in foes:
                    # generate a new temporary attacker unit object
                    tmp_target = copy.deepcopy(tmp_tgt)
                    # set the number of attacks for the upcoming fight
                    tmp_target.a = ff[1]
                    # reset the counter for the temporary unit
                    tmp_target.causedWounds = 0
                    tmp_target.causedOOA = 0

                    if tmp_target.inconsistency == True:
                        print "\n---- " + tmp_target.name + " stats for this fight"
                        printChar(tmp_target)
                        print "----"

                    # set the new pre state
                    ff[0].pre_state = ff[0].state

                    # generate a new temporary unit which is the target
                    tmp_ff = copy.deepcopy(ff[0])
                    # reset the counter for the temporary unit
                    tmp_ff.causedWounds = 0
                    tmp_ff.causedOOA = 0

                    # do the fight
                    doFight(tmp_target, tmp_ff)

                    # summarize the result of the fight
                    ff[0].causedWounds = ff[0].causedWounds + tmp_ff.causedWounds
                    ff[0].causedOOA = ff[0].causedOOA + tmp_ff.causedOOA
                    ff[0].state = tmp_ff.state
                    ff[0].w = tmp_ff.w
                    ff[0].i_orig = tmp_ff.i_orig
                    ff[0].i = tmp_ff.i
                    ff[0].luckyCharmUsed = tmp_ff.luckyCharmUsed
                    ff[0].luckyCharm = tmp_ff.luckyCharm
                    tmp_tgt.causedWounds = tmp_tgt.causedWounds + tmp_target.causedWounds
                    tmp_tgt.causedOOA = tmp_tgt.causedOOA + tmp_target.causedOOA
                    tmp_tgt.i_orig = tmp_tgt.i_orig
                    tmp_tgt.i = tmp_tgt.i
                    tmp_tgt.w = tmp_tgt.w
                    tmp_tgt.state = tmp_tgt.state
                    tmp_tgt.luckyCharmUsed = tmp_target.luckyCharmUsed
                    tmp_tgt.luckyCharm = tmp_target.luckyCharm

                    if tmp_tgt.state == 3:
                        break # the target is already ooa

                first_round = False

        else:

            # recovery phase
            tmp_first_line = True
            for u in all_fighters:

                do_recover = False
                if u.name == target.name and ((rounds + 1) % 2) == 0:
                   do_recover = True
                elif u.name != target.name and ((rounds + 1) % 2) == 1:
                   do_recover = True

                if do_recover == True:
                   if u.state == 1:
                        if tmp_first_line == True:
                            print "\n\n---"
                        u.state = 0
                        u.i_orig = u.i
                        u.i = -9 # strike last
                        tmp_first_line = False
                        print "\t" + u.name + ": stand up"
                   if u.state == 2:
                        if tmp_first_line == True:
                            print "\n\n---"
                        u.state = 1
                        u.i_orig = u.i
                        u.i = -9 # strike last
                        tmp_first_line = False
                        print "\t" + u.name + ": stn -> knd"

            if tmp_first_line == False:
                print "---"

            fights_ini_ordered = []
            # 1. liste fer kampfenden nach ini sortieren
            fights_ini_ordered = sorted(all_fighters, key=lambda x: x.i, reverse=True)

            print "\nfight order:"
            for t in fights_ini_ordered:
            	print "\t" + t.name + " " + str(t.i)
            print

            #for fo in fights_ini_ordered:
            #    print fo.name + " " + str(fo.i)

            # 2. die kampfe ausfuhren
            for f in fights_ini_ordered:
                if tmp_tgt.state == 3:
                    break # the target is ooa, abort all fights

		if f.i == -9:
			f.i = f.i_orig

                if f.name != target.name:
                    if f.state == 0:
                        tmp_tgt.pre_state = tmp_tgt.state
                        doFight(f, tmp_tgt)

                else:
                    if f.state == 0:
                        # 3. choose f.A foes if has more than one
                        print "---- " + tmp_tgt.name + " (" + getStrState(tmp_tgt.state) + "): selected foes to attack (" + str(tmp_tgt.a) + "A possible)"

                        foes = []
                        tmp_doNotUseOffhand = False
                        for i in range(f.a):
                            j = random.randint(0, len(tmp_att)-1)
                            l = 0
                            while (tmp_att[j].state > 0 and l < 50) or tmp_att[j].cantBeAttacked == True:
                                j = random.randint(0, len(tmp_att)-1)
                                l = l + 1

                            if l == 50:
                                l = 0
                                j = random.randint(0, len(tmp_att)-1)

                                while (tmp_att[j].state == 3 and l < 50) or tmp_att[j].cantBeAttacked == True:
                                    j = random.randint(0, len(tmp_att)-1)
                                    l = l + 1

                                if l == 50:
                                    for j in range(len(tmp_att)):
                                        if tmp_att[j].state < 3:
                                            break
                                            #exit(0) # TODO fix target selection bug here

                            print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state)

                            tmp_inc = False # flag which indicates if the attack has been added to the choosen attacker
                            for k in range(len(foes)):
                                if foes[k][0] == tmp_att[j]:
                                    if tmp_doNotUseOffhand == False:
                                        foes[k][0].doNotUseOffhand = True if random.randint(0,1) else False
                                        tmp_doNotUseOffhand = True
                                        if tmp_tgt.weapon[0]["offhand"] == True or \
                                           (len(tmp_tgt.weapon) > 1 and \
                                            tmp_tgt.weapon[1]["offhand"] == True):
                                          print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state) + " off hand attack"

                                    foes[k][1] = foes[k][1] + 1
                                    tmp_inc = True
                                    break

                            if tmp_inc == False:
                                foes.append([tmp_att[j], 1])
                                if tmp_doNotUseOffhand == False:
                                    foes[-1][0].doNotUseOffhand = True if random.randint(0,1) else False
                                    tmp_doNotUseOffhand = True
                                    if tmp_tgt.weapon[0]["offhand"] == True or \
                                       (len(tmp_tgt.weapon) > 1 and \
                                        tmp_tgt.weapon[1]["offhand"] == True):
                                      print "\t" + tmp_att[j].name + " St = " + getStrState(tmp_att[j].state) + " off hand attack"

                        for ff in foes:
                            # generate a new temporary attacker unit object
                            tmp_target = copy.deepcopy(tmp_tgt)

                            # set the number of attacks for this fight
                            tmp_target.a = ff[1]

                            # reset the counter for the temporary unit
                            tmp_target.causedWounds = 0
                            tmp_target.causedOOA = 0

                            print "\n---- " + tmp_target.name + " stats for this fight"
                            printChar(tmp_target)
                            print "----"

                            ff[0].pre_state = ff[0].state

                            # generate the temporary target unit object
                            tmp_ff = copy.deepcopy(ff[0])

                            # reset the counter for the temporary unit
                            tmp_ff.causedWounds = 0
                            tmp_ff.causedOOA = 0

                            # do the fight
                            doFight(tmp_target, tmp_ff)

                            # sumamrize the result of the fight
                            ff[0].causedWounds = ff[0].causedWounds + tmp_ff.causedWounds
                            ff[0].causedOOA = ff[0].causedOOA + tmp_ff.causedOOA
                            ff[0].state = tmp_ff.state
                            ff[0].i = tmp_ff.i
                            ff[0].i_orig = tmp_ff.i_orig
                            ff[0].w = tmp_ff.w
                            ff[0].luckyCharmUsed = tmp_ff.luckyCharmUsed
                            ff[0].luckyCharm = tmp_ff.luckyCharm
                            tmp_tgt.causedWounds = target.causedWounds + tmp_target.causedWounds
                            tmp_tgt.causedOOA = target.causedOOA + tmp_target.causedOOA
                            tmp_tgt.w = tmp_target.w
                            tmp_tgt.state = tmp_target.state
                            tmp_tgt.luckyCharmUsed = tmp_target.luckyCharmUsed
                            tmp_tgt.luckyCharm = tmp_target.luckyCharm
                            tmp_tgt.i = tmp_target.i
                            tmp_tgt.i_orig = tmp_target.i_orig
                            if tmp_tgt.state == 3:
                                break # the target is down, abort the fight

        print "========="
        rounds = rounds + 1

    print "\n--------------------"
    print str(rounds) + " rounds done"
    for u in tmp_att:
        printChar(u)
    printChar(tmp_tgt)
    print

    return [ tmp_att, tmp_tgt, rounds ]

@synchronized
def runSimulation():

    statistic = []

    if args.quiet == True:
        printChar(target)
        for a in attackers:
            printChar(a)
        print

        blockPrint()

    for i in range(args.max_tries):
        statistic.append( fightTilOOA([ copy.deepcopy(attackers), copy.deepcopy(target) ]) )

    return statistic

def printStatistic(statistic):

    cnt_knd = 0
    cnt_stn = 0
    cnt_ooa = 0
    cnt_cw = 0
    cnt_cooa = 0
    tmp_stat_attackers = []
    max_run = args.max_tries
    tmp_rounds = 0

    for s in statistic:
        tmp_rounds = tmp_rounds + s[2]

    for j in range(len(attackers)):
        tmp_stat_attackers.append([ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ])

    for i in range(max_run):
        if statistic[i][1].state == 1:
          cnt_knd = cnt_knd + 1
        if statistic[i][1].state == 2:
          cnt_stn = cnt_stn + 1
        if statistic[i][1].state == 3:
          cnt_ooa = cnt_ooa + 1

        cnt_cw = cnt_cw + statistic[i][1].causedWounds
        cnt_cooa = cnt_cooa + statistic[i][1].causedOOA

        for j in range(len(attackers)):

            tmp_stat_attackers[j][0] = tmp_stat_attackers[j][0] + statistic[i][0][j].causedWounds / (max_run * 1.0)
            #print attackers[j].name + " == " + statistic[i][0][j].name + ": " + str(statistic[i][0][j].causedWounds)
            tmp_stat_attackers[j][1] = tmp_stat_attackers[j][1] + statistic[i][0][j].causedOOA / (max_run * 1.0)
            #print attackers[j].name + " == " + statistic[i][0][j].name + ": " + str(statistic[i][0][j].causedOOA)
            if statistic[i][0][j].state == 0:
                tmp_stat_attackers[j][2] = tmp_stat_attackers[j][2] + 1 / (max_run * 1.0) # count normal state
            if statistic[i][0][j].state == 1:
                tmp_stat_attackers[j][3] = tmp_stat_attackers[j][3] + 1 / (max_run * 1.0) # count knocked down
            if statistic[i][0][j].state == 2:
                tmp_stat_attackers[j][4] = tmp_stat_attackers[j][4] + 1 / (max_run * 1.0) # count stunned
            if statistic[i][0][j].state == 3:
                tmp_stat_attackers[j][5] = tmp_stat_attackers[j][5] + 1 / (max_run * 1.0) # count ooA

    #print cnt_cooa
    #print cnt_cw
    cnt_knd = cnt_knd   / (max_run * 1.0)
    cnt_stn = cnt_stn   / (max_run * 1.0)
    cnt_ooa = cnt_ooa   / (max_run * 1.0)
    cnt_cw = cnt_cw     / (max_run * 1.0)
    cnt_cooa = cnt_cooa / (max_run * 1.0)

    enablePrint()
    sum_state_norm   = 0
    sum_state_knd    = 0
    sum_state_stn    = 0
    sum_state_ooa    = 0
    for j in range(len(attackers)):

        print "\n" + attackers[j].name + "\n====="
        print "caused wound " + str(tmp_stat_attackers[j][0] * 100.0) + " %"
        print "caused ooA   " + str(tmp_stat_attackers[j][1] * 100.0) + " %"
        print "state normal " + str(tmp_stat_attackers[j][2] * 100.0) + " %"
        print "state knd    " + str(tmp_stat_attackers[j][3] * 100.0) + " %"
        print "state stn    " + str(tmp_stat_attackers[j][4] * 100.0) + " %"
        print "state ooA    " + str(tmp_stat_attackers[j][5] * 100.0) + " %"

        sum_state_norm   = sum_state_norm   + tmp_stat_attackers[j][2] * 100.0
        sum_state_knd    = sum_state_knd    + tmp_stat_attackers[j][3] * 100.0
        sum_state_stn    = sum_state_stn    + tmp_stat_attackers[j][4] * 100.0
        sum_state_ooa    = sum_state_ooa    + tmp_stat_attackers[j][5] * 100.0

    print "\n=========="
    print "unit count (" + str(len(attackers)) + ") / state per warband"
    print "normal " + str(sum_state_norm / 100.0)
    print "knd    " + str(sum_state_knd  / 100.0)
    print "stn    " + str(sum_state_stn  / 100.0)
    print "ooA    " + str(sum_state_ooa  / 100.0)

    print "\n=========="
    print "average rounds " + str(tmp_rounds / (max_run * 1.0))
    print

    print target.name + " (" + str(max_run) + " tries)"
    print "=========="
    print "OOA in about " + str(cnt_ooa * (100.0)) + " %"
    print "Caused a wound " + str(cnt_cw * 100.0) + " %"
    print "Caused ooA " + str(cnt_cooa * 100.0) + " %"
    print

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

if __name__ == "__main__":

    args = parser.parse_args()

    statistic = runSimulation()

    printStatistic(statistic)

