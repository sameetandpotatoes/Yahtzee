import random #to generate random dice
import pickle #to save high score
import os #to help clear the screen
import time
from colorama import *
init(autoreset=True)

class bcolors:
    HEADER = Fore.MAGENTA
    OKBLUE = Fore.BLUE
    OKGREEN = Fore.GREEN
    WARNING = Fore.BLACK
    FAIL = Fore.RED
    ENDC = Fore.RESET

turnNumber = 0
scoreOfPlayer = 0 #global variable to keep track of score
finalRoll = []
allKeysandValues = {}
bonusReceived = False
yahtzeeOnce = False #so players select an option only once
#This method rolls finalRoll and keeps track of which finalRoll players want to keep
def roll():
	global finalRoll
	finalRoll = rolldie(5) #for first roll
	replacing = []
	indexesused = []
	times = 0
	print(bcolors.OKGREEN + "Your first roll was:", finalRoll, "\n")
	result = input(bcolors.HEADER + "Do you want to keep these dice? (y or n) " + bcolors.ENDC)
	result = (result.lower()).strip()
	while result not in ("y", "n"):
		result = input(bcolors.FAIL + "\nYou probably mistyped something. Try again. " + bcolors.ENDC)
		result = (result.lower().strip())
	if result == "n":
	    while times != 2:
	        if times != 0:
	            print(bcolors.OKGREEN + "Your current dice are:", finalRoll, "\n")
	            result = input(bcolors.HEADER + "Do you want to keep these dice (y or n) (default answer is n)? " + bcolors.ENDC)
	            result = (result.lower()).strip()
	            if result == "y":
	            	break;
	        indexes = input(bcolors.HEADER + "Type the ordinal numbers (first would be 1, second would be 2, and so on)\nof what you want to replace. (no spaces) " + bcolors.ENDC)
	        try:
	        	indexesList = list(indexes)
	        	for index in indexesList:
	        		index = int(index)
	        		while index in indexesused:
	        			print(bcolors.FAIL + "Sorry, you are already replacing " + str(finalRoll[index - 1]) + ".\n")
	        			index = input(bcolors.FAIL + "Try another index. " + bcolors.ENDC)
	        			index = int(index)
	        		replacing.append(index - 1)
	        		indexesused.append(index)
	        		#The following line makes sure that the index called was okay
	        		finalRoll[index - 1]
	        except IndexError:
	            print(bcolors.FAIL + "\nYou only have 5 dice!\n" + bcolors.ENDC)
	            replacing = []
	            indexesused = []
	            continue
	        except:
	            print(bcolors.FAIL + "\nYou probably mistyped something. Try again.\n" + bcolors.ENDC)
	            replacing = []
	            indexesused = []
	            continue
	        if len(replacing) == 0:
	            print(bcolors.OKGREEN + "Not replacing anything. Keeping all dice ..." + bcolors.ENDC)
	            break;
	        else:
	        	numReplacing =[]
	        	for index in replacing:
	        		numReplacing.append(finalRoll[index])
	        	if len(replacing) == 5:
	        		numReplacing = "everything"
	        	print(bcolors.OKBLUE + "Replacing", numReplacing , "" + bcolors.ENDC)
	        keeping = []
	        for index in (set([0,1,2,3,4]) - set(replacing)):
	        	keeping.append(finalRoll[index])

	        newfinalRollarray = rolldie(len(replacing))
	        for newfinalRoll in newfinalRollarray:
	            keeping.append(newfinalRoll)

	        finalRoll = keeping
	        replacing = []
	        indexesused = []
	        times += 1
	print(bcolors.OKGREEN + "\nYour roll was: %s\n" %(finalRoll) + bcolors.ENDC)

def rolldie(numToRoll):
    diechoices = ['1', '2', '3', '4', '5', '6']
    result = []
    for x in range(numToRoll):
        result.append(int(random.choice(diechoices)))
    return result

def countDice(number):
	counter = 0
	for n in finalRoll:
		if n == number:
			counter = counter + 1
	score = counter * number
	return score

def choosePoints():
	key = allValues[0]
	value = allValues[1]
	bestOption = max(value)
	counter = 1;
	for index in range(0, len(key)):
		if value[index] == bestOption:
			print('\033[1m'+ str(counter) + ":\t", end="")
			print(str(key[index]) + ":\t" + str(value[index]) + " points" + '\033[0m')
		else:
			print(str(counter) + ":\t", end="")
			print(str(key[index]) + ":\t" + str(value[index]) + " points.")
		counter += 1
	global scoreOfPlayer
	global allKeysTaken
	option = input(bcolors.HEADER + "\nHere are all of your options to pick from. Choose which one you would like by entering the name or number of the option.\n" + bcolors.ENDC)
	while True:
		try:
			option = key[int(option) - 1]
		except:
			pass
		for index in range(0, len(key)):
			keycopy = (key[index].strip(" ")).lower()
			option = (option.strip()).lower()
			if keycopy == option:
				scoreOfPlayer = scoreOfPlayer + int(value[index])
				allKeysandValues[key[index]] = int(value[index])
				return;
		option = input(bcolors.FAIL + "You probably mistyped something. Try again.\n" + bcolors.ENDC)

def checkFullHouse():
	for num in finalRoll:
		if finalRoll.count(num) == 3:
			for second_num in finalRoll:
				if finalRoll.count(second_num) == 2:
					return 25
	return 0

def ofAKind(numOfKind):
	global yahtzeeOnce
	for number in finalRoll:
		if finalRoll.count(number) == numOfKind:
			if numOfKind == 5: #Yahtzee
				if yahtzeeOnce: #Second Yahtzee
					return 100;
				else: #First Yahtzee
					yahtzeeOnce = True
					return 50
			else:
				return numOfKind * number
	return 0
def checkStraight(smallOrLarge):
	sortedArray = list(set(finalRoll))
	if smallOrLarge == 1: #large
		if [1,2,3,4,5] == sortedArray or [2,3,4,5,6] == sortedArray:
			return 40
	else: #type = 0, small
		if all(x in sortedArray for x in [1,2,3,4]) or all(x in sortedArray for x in [2,3,4,5]) or all(x in sortedArray for x in [3,4,5,6]):
			return 30
	return 0

def removeTakenOptions():
	#Gather all zeros first
	key = allValues[0]
	value = allValues[1]
	#indexesToDelete = []
	index = len(key) - 1
	while index >= 0:
		if "Pass          " not in key[index]:
			int(value[index])
			if value[index] == 0:
				del key[index]
				del value[index]
		index -= 1
	#Gather already taken choices
	global allKeysandValues
	for takenKey in allKeysandValues.keys():
		index = len(key) - 1
		while index >= 0:
			if "Pass          " not in takenKey:
				if takenKey is key[index]:
					del key[index]
					del value[index]
			index -= 1
def over63():
	global bonusReceived
	if bonusReceived:
		return False;
	global allKeysandValues
	sumOfFirstSix = 0
	arrayToCheck = ['Ones          ', 'Twos          ', 'Threes        ',
					 'Fours         ', 'Fives         ', 'Sixes         ']
	if all(x in list(allKeysandValues.keys()) for x in arrayToCheck):
		for index in arrayToCheck:
			sumOfFirstSix += int(allKeysandValues[index])
	if sumOfFirstSix >= 63:
		bonusReceived = True
		return True
	else:
		return False

def printCurrentScoreCard(allOptions):
	global scoreOfPlayer
	printedBonus = True
	print(bcolors.HEADER + "Yahtzee Score Card" + bcolors.ENDC)
	for key in allOptions:
		if key == "Over 63 = +35 ":
			print(bcolors.OKBLUE + key + "|\t" + bcolors.ENDC, end = "")
		elif key != "Pass          ":
			print(bcolors.OKBLUE + key + "|\t" + bcolors.ENDC, end="")
		for k, v in allKeysandValues.items():
			if k == key and k != "Pass          ": #already taken
				print(bcolors.OKGREEN + str(v), end = "")
			if key == "Over 63 = +35 ":
				if over63():
					scoreOfPlayer += 35
				if bonusReceived and printedBonus:
					print(bcolors.OKGREEN + "35" + bcolors.ENDC, end = "")
					printedBonus = False
		print()
	print("Current Score: " + str(scoreOfPlayer))

#Where the program starts
try:
	inFile = open("highscores.dat", "rb")
	highScore = pickle.load(inFile)
	print(bcolors.HEADER + "Your high score was: " + str(highScore) + ". Try to beat it!")
except EOFError:
	pass
for turnNumber in range(13):
	print(bcolors.HEADER+ "Turn %s started.\n" %(turnNumber + 1) + bcolors.ENDC)
	roll()

	allValues = [   ["Ones          ", "Twos          ", "Threes        ",
					 "Fours         ", "Fives         ", "Sixes         ",
					 "Over 63 = +35 ",
					 "3 of a kind   ", "4 of a kind   ", "Full House    ",
					 "Small Straight", "Large Straight", "Yahtzee       ",
					 "Chance        ", "Pass          "],
					[countDice(1), countDice(2), countDice(3),
					 countDice(4), countDice(5), countDice(6), 0,
					 ofAKind(3), ofAKind(4), checkFullHouse(),
					 checkStraight(0), checkStraight(1), ofAKind(5),
					 sum(finalRoll), 0]]
	allKeys = allValues[0].copy()
	removeTakenOptions()
	choosePoints()
	time.sleep(0.5) #Sleep for one second
	os.system('cls' if os.name=='nt' else 'clear') #Will work on both Unix and Windows
	print(bcolors.HEADER + "\nTurn", turnNumber + 1, "completed." + bcolors.ENDC)
	print(bcolors.OKGREEN + "Here is your current Score Card:\n\n" + bcolors.ENDC)
	printCurrentScoreCard(allKeys)

#End of game
print(bcolors.HEADER + "Game Over! Your score was: " + str(scoreOfPlayer) + bcolors.ENDC)
outFile = open("highscores.dat", "wb")
try:
	if scoreOfPlayer > highScore:
		highScore = scoreOfPlayer
	pickles.dump(highScore, outFile)
except NameError: #This means it was the first time this game has been played
	pickle.dump(scoreOfPlayer, outFile)
outFile.close()


