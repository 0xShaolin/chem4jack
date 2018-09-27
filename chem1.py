#ur welcome jack. luv u

try:
	import sys
	from termcolor import colored
except ImportError:
	print "I thought you had termcolor"
	print "i'm installing it 4 u silently, pls dont ctrl c"
	os.system('pip install termcolor > /dev/null 2>&1')
	from termcolor import colored

def intro():
	print "you need help so let me help u"
	print "ur lucky im good at chem"
	print "also round up, i am too lazy to make the ints floats"

def calc2():
	print "first we will identify the limiting reactant."
	numofreactants = raw_input('how many reactants? ')
	if numofreactants == '1':
		print "there is no limiting reactant."
	elif numofreactants == '2':
		print "you will have 1 limiting reactant."
		print "for reactant 1:"
		gramspmol1 = raw_input('how many grams per mol? ')
		gramspmol1 = int(gramspmol1)
		gramshad1 = raw_input('how many grams do you have? ')
		gramshad1 = int(gramshad1)
		ratio1 = float(gramshad1/gramspmol1)
		print "for reactant 2:"
		gramspmol2 = raw_input('how many grams per mol? ')
		gramshad2 = raw_input('how many grams do you have? ')
		gramspmol2 = int(gramspmol2); gramshad2 = int(gramshad2)
		ratio2 = float(gramshad2/gramspmol2)
		if ratio1 > ratio2:
			print "reactant 2 is the limiting reactant"
			gramsreacting = float(gramspmol1*ratio2)
			print "only " + str(gramsreacting) + " of reactant 1 will be used"
		elif ratio1 < ratio2:
			print "reactant 1 is the limiting reactant"
			gramsreacting = float(gramspmol2*ratio1)
			print "only " + str(gramsreacting) + " of reactant 2 will be used"
		elif ratio1 == ratio2:
			print "there is no limiting reactant."
			print "both values will be run to 0."

def calc1():
	numofreactants = raw_input('how many reactants? ')
	print "The number of reactants is: " + numofreactants
	if numofreactants == '1':
		print "come on now son."
	elif numofreactants == '2':
		print "for the known reactant:"
		gramspmol1 = raw_input('how many grams per mol? ')
		gramshad1 = raw_input('how many grams do you have? ')
		gramshad1 = int(gramshad1); gramspmol1 = int(gramspmol1)
		ratio = float(gramshad1/gramspmol1)
		print "for the unknown reactant:"
		gramspmol2 = raw_input('how many grams per mol? ')
		gramspmol2 = int(gramspmol2)
		gramsneeded = float(gramspmol2*ratio)
		print "the grams needed for the unknown reactant are: " + str(gramsneeded)
	elif numofreactants == '3':
		print "pick the known reactant who's grams per mol is easiest to calculate."
		print "for that reactant:"
		gramspmol1 = raw_input('how many grams per mol? ')
		gramshad1 = raw_input('and how many grams do you have? ')
		gramshad1 = int(gramshad1); gramspmol1 = int(gramspmol1)
		ratio = float(gramshad1/gramspmol1)
		print "for one of the other reactants:"
		gramspmol2 = raw_input('how many grams per mol? ')
		print "and for the last reactant:"
		gramspmol3 = raw_input('how many grams per mol ')
		gramspmol2 = int(gramspmol2); gramspmol3 = int(gramspmol3)
		gramsneeded1 = float(gramspmol2*ratio)
		gramsneeded2 = float(gramspmol3*ratio)
		print "for the second reactant, you need: " + str(gramsneeded1)
		print "for the third reactant, you need: " + str(gramsneeded2)

def main():
	print "(1) calculate grams needed to react"
	print "(2) limiting reactants"
	print "(quit) (exit)"
	choice = raw_input('which opt? ')
	if choice == 'quit' or choice == 'exit':
		exit(1)
	elif choice == '1':
		calc1()
	elif choice == '2':
		calc2()
	else:
		print "command not found"

intro()
while 1:
	try:
		main()
	except KeyboardInterrupt:
		exit(1)

