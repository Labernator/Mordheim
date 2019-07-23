
import random

from deco import *

from simu import rollD6, getMinWoundRoll, printChar, enablePrint, blockPrint, printStatistic_
from simu_unit import *

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

def getToHit(bs):
	if bs == 0:
		return 7
	elif bs == 1:
		return 6
	elif bs == 2:
		return 5
	elif bs == 3:
		return 4
	elif bs == 4:
		return 3
	elif bs == 5:
		return 2
	elif bs == 6:
		return 1
	else:
		return 0

def tryToHit(attacker, target):

	if target.state == 2: # stunned
		print "\t\tauto hit & wound -> ooA"
		target.state = 3
		attacker.causedOOA = attacker.causedOOA + 1
		return

	roll = rollD6()
	tohit = getToHit(attacker.bs)
	print "\tto hit on: " + str(tohit)
	print "\thit roll: " + str(roll)

	if target.state == 1: # knocked down
		if roll >= tohit:
			print "\thit"
			print "\t\tauto wound -> ooA"
			target.state = 3
			attacker.causedOOA = attacker.causedOOA + 1
			return

        if roll >= tohit:
		print "\thit"

		tryToWound(attacker, target)
	else:
		print "\tno hit"

def armorSaveGranted(s, _as):

	tmp_as = _as
	tmp_s = s - 3
	if tmp_s > 0:
		tmp_as = tmp_as + tmp_s
	print "\t\t\tarmor save on: " + str(tmp_as)

	if tmp_as < 7:
		roll = rollD6()
		print "\t\t\troll: " + str(roll)
		if roll >= tmp_as:
			print "\t\t\tgranted"
			return True

	print "\t\t\tno armor save"

	return False

def tryToWound(attacker, target):
	roll = rollD6()
	towound = getMinWoundRoll(attacker.rs, target.t)
        print "\t\tto wound on: " + str(towound)
	print "\t\twound roll: " + str(roll)
        if roll >= towound:
		if roll == 6:
			print "\t\tcrit"
		# armour saves
		no_as = True
		if target._as > 0:
			no_as = not armorSaveGranted(attacker.rs, target._as)
			if no_as == False:
				print "\t\tno wound"

		if no_as == True:
			print "\t\twound"
			target.w = target.w - 1
			attacker.causedWounds = attacker.causedWounds + 1
			if target.w == 0:
				# try to injure
				roll = rollD6()
				print "\t\t\tinjury roll: " + str(roll)
				if roll < 3:
					target.state = 1
					print "\t\t\tknocked down"
				elif roll < 5:
					target.state = 2 
					print "\t\t\tstunned"
				else:
					target.state = 3
					attacker.causedOOA = attacker.causedOOA + 1
					print "\t\t\tout of action"

	else:
		print "\t\tno wound"

@concurrent
def doShooting(tmp_data):

	at = tmp_data[0]
	ta = tmp_data[1]
	r = 1
	#print ta.state
	while ta.state < 3:
		print "Round " + str(r) + "\n====================\n"

		for a in at:
			if a.bs == 0:
				continue # skip units without ballistic skill
			if ta.state > 2: # ooA
				break
			#print a.name + " vs " + target.name
			printChar(a)
			printChar(ta)
			print

			tryToHit(a, ta)
			print

			printChar(a)
			printChar(ta)
			print
		r = r + 1

	return [at, ta, r]

@synchronized
def doAllTries():
	statistic = []
	for i in range(args.max_tries):
		#print "--- try " + str(i) + " ---"
		tmp_attackers = copy.deepcopy(attackers)
		tmp_target = copy.deepcopy(target)
		#print tmp_target.state

		statistic.append( doShooting([tmp_attackers, tmp_target]) )

	return statistic

if __name__ == "__main__":

	args = parser.parse_args()

	if args.quiet == True:
		blockPrint()

	statistic = doAllTries()

	enablePrint()

	printStatistic_(statistic, args.max_tries)

