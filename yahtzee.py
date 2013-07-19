import random #to generate random finalRoll
import pickle #to save high score
import os #to help clear the screen
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

scoreOfPlayer = 0 #global variable to keep track of score
finalRoll = []
allKeysTaken = [] #so players can select an option only once
#This method rolls finalRoll and keeps track of which finalRoll players want to keep
def roll():
	global finalRoll
	finalRoll = rolldie(5) #for first roll
	replacing = []
	indexesused = []
	times = 0
	print(bcolors.HEADER + "Your first roll was:", finalRoll, "\n")
	result = input("Are you going to keep all or replace some? (k or r) " + bcolors.ENDC)
	result = (result.lower()).strip()
	while result not in ("k", "r"):
		result = input(bcolors.FAIL + "\nYou probably mistyped something. Try again. " + bcolors.ENDC)
		result = (result.lower().strip())     
	if result == "r":
	    while times != 2:
	        if times != 0:
	            print("Your current dice are:", finalRoll, "\n")
	            result = input(bcolors.HEADER + "Do you want to keep these dice (y or n) (default answer is y)? " + bcolors.ENDC)
	            result = (result.lower()).strip()
	            if result == "y":
	            	break;
	        indexes = input(bcolors.HEADER + "Type the ordinal numbers (first would be 1, second would be 2, and so on)\n of what you want to replace. (no spaces)" + bcolors.ENDC)
	        try:
	        	indexesList = list(indexes)
	        	for index in indexesList:
	        		index = int(index)
	        		while index in indexesused:
	        			print(bcolors.FAIL + "Sorry, you are already replacing " + str(finalRoll[index - 1]) + ".\n")
	        			index = input("Try another index. " + bcolors.ENDC)
	        			index = int(index)
	        		replacing.append(index - 1)
	        		indexesused.append(index)
	        except IndexError:
	            print(bcolors.FAIL + "\nYou only have 5 finalRoll!\n" + bcolors.ENDC)
	            replacing = []
	            indexesused = []
	            continue
	        except:
	            print(bcolors.FAIL + "\nYou probably mistyped something. Remember: don't include spaces!\n" + bcolors.ENDC)
	            replacing = []
	            indexesused = []
	            continue
	        if len(replacing) == 0:
	            print(bcolors.OKGREEN + "Not replacing anything. Rerolling all dice ..." + bcolors.ENDC)
	        else:
	        	numReplacing =[]
	        	for index in replacing:
	        		numReplacing.append(finalRoll[index])
	        	print(bcolors.OKBLUE + "Replacing", numReplacing , "and rolling the others ..." + bcolors.ENDC)
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
	print(bcolors.OKGREEN + "Your roll was: %s\n" %(finalRoll) + bcolors.ENDC)

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
    for key, value in list(allValues.items()):
        key = str(key)
        value = str(value)
        print(key + ":\t" + value + " points.")
    global scoreOfPlayer
    global allKeysTaken
    option = input(bcolors.HEADER + "\nHere are all of your options to pick from. Choose which one you would like by entering the name of the option.\n" + bcolors.ENDC)
    while True:
	    for key, value in allValues.items():
	        keycopy = (key.strip(" ")).lower()
	        option = (option.strip()).lower()
	        if keycopy == option:
	        	scoreOfPlayer = scoreOfPlayer + int(value)
	        	print(bcolors.OKBLUE + "\nPlayer Score: %s\n" %(scoreOfPlayer) + bcolors.ENDC)
	        	allKeysTaken.append(key)
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
	for number in finalRoll:
		if finalRoll.count(number) == numOfKind:
			if numOfKind == 5:
				return 50
			else:
				return numOfKind * number
	return 0
def checkStraight(smallOrLarge):
	sortedArray = list(set(finalRoll))
	if smallOrLarge == 1: #large
		if [1,2,3,4,5] == sortedArray or [2,3,4,5,6] == sortedArray:
			return sum(finalRoll)
	else: #type = 0, small 
		if all(x in sortedArray for x in [1,2,3,4]) or all(x in sortedArray for x in [2,3,4,5]) or all(x in sortedArray for x in [3,4,5,6]):
			return sum(finalRoll)
	return 0

def removeTakenOptions():
	keysToPop = []
	#Gather all zeros first
	for key, value in allValues.items():
		value =  int(value)
		if "Pass          " not in key:
			if value == 0:
				keysToPop.append(key)
	#Gather already taken choices
	global allKeysTaken
	for key in allKeysTaken:
		for keys, values in list(allValues.items()):
			values = int(values)
			if "Pass          " not in key:
				if key is keys:
					keysToPop.append(key)
	#Remove everything gathered
	try:
		for key in keysToPop:
			if key in allValues.keys():
				allValues.pop(key)
	except KeyError:
		pass

#Main method
try:
	inFile = open("highscores.dat", "rb")
	highScore = pickle.load(inFile)
	print("Your high score was: " + str(highScore) + ". Try to beat it!")
except EOFError:
	pass
for turns in range(10):
	print(bcolors.HEADER+ "Turn %s started.\n" %(turns + 1) + bcolors.ENDC)
	roll()
	allValues = {    "Ones          " : countDice(1),
                     "Twos          " : countDice(2),
                     "Threes        " : countDice(3),
                     "Fours         " : countDice(4),
                     "Fives         " : countDice(5),
                     "Sixes         " : countDice(6),
                     "3 of a kind   " : ofAKind(3),
                     "4 of a kind   " : ofAKind(4),
                     "Full House    " : checkFullHouse(),
                     "Small Straight" : checkStraight(0),
                     "Large Straight" : checkStraight(1),
                     "Yahtzee       " : ofAKind(5),
                     "Chance        " : sum(finalRoll),
                     "Pass          " : 0}
	removeTakenOptions()
	choosePoints()
	
	time.sleep(1) #Sleep for one second
	os.system('cls' if os.name=='nt' else 'clear') #Will work on both Unix and Windows
	print(bcolors.HEADER + "\nTurn", turns + 1, "completed." + bcolors.ENDC)

print(bcolors.HEADER + "Game Over! Your score was: " + str(scoreOfPlayer) + bcolors.ENDC)
outFile = open("highscores.dat", "wb")
try:
	if scoreOfPlayer > highScore:
		highScore = scoreOfPlayer
	pickles.dump(highScore, outFile)
except NameError: #This means it was the first time this game has been played
	pickle.dump(scoreOfPlayer, outFile) 

outFile.close()


