import random
scoreOfPlayer = 0
allKeysTaken = []
def roll():
    finalroll = rolldie(5)
    keeping = []
    indexesused = []
    
    print("Your first roll was:", finalroll, "\n")
    result = input("Are you going to keep all or replace some? (k or r) ")
    result = (result.lower()).strip()
    while result not in ("k", "r"):
    	result = input("\nYou probably mistyped something. Try again. ")
    	result = (result.lower().strip())     
    if result == "r":
        for times in range(2):
            if times != 0:
	            print("Your current dice are:", finalroll)
	            result = input("Do you want to keep these dice (y or n) (default answer is y)? ")
	            result = (result.lower()).strip()
	            if result != "n":
	            	break;
            indexes = input("Type the numbers of what you want to keep. (no spaces)")
            try:
            	indexesList = list(indexes)
            	for index in indexesList:
            		index = int(index)
            		while index in indexesused:
            			print("Sorry, you are already replacing " + str(finalroll[index - 1]) + ".\n")
            			index = input("Try another index. ")
            			index = int(index)
            		keeping.append(finalroll[index - 1])
            		indexesused.append(index)
            except IndexError:
                print("\nYou only have 5 dice!\n")
                continue
            except:
                print("\nYou probably mistyped something. Remember: don't include spaces!\n")
                continue
            if len(keeping) == 0:
                print("Not keeping anything. Rerolling all dice ...")
            else:
                print("Keeping", keeping, "and rolling the others ...")
            newdicearray = rolldie(5-len(keeping))
            for newdice in newdicearray:
                keeping.append(newdice)
            
            finalroll = keeping
            keeping = []
            indexesused = []
    print("Your roll was: %s\n" %(finalroll))
    return finalroll

def rolldie(numToRoll):
    diechoices = ['1', '2', '3', '4', '5', '6']
    result = []
    for x in range(numToRoll):
        result.append(int(random.choice(diechoices)))
    return result

def countDice(number):
	counter = 0
	for n in dice:
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
    option = input("\nHere are all of your options to pick from. Choose which one you would like by entering the name of the option.\n")
    while True:
	    for key, value in allValues.items():
	        keycopy = (key.strip(" ")).lower()
	        option = (option.strip()).lower()
	        if keycopy == option:
	        	scoreOfPlayer = scoreOfPlayer + int(value)
	        	print("\nPlayer Score: %s\n" %(scoreOfPlayer))
	        	allKeysTaken.append(key)
	        	return;
	    option = input("You probably mistyped something. Try again.\n")
    
def checkFullHouse():
	for num in dice:
		if dice.count(num) == 3:
			for second_num in dice:
				if dice.count(second_num) == 2:
					return 25
	return 0

def ofAKind(numOfKind):
	for number in dice:
		if dice.count(number) == numOfKind:
			if numOfKind == 5:
				return 50
			else:
				return numOfKind * number
	return 0
def checkStraight(smallOrLarge):
	sortedArray = list(set(dice))
	if smallOrLarge == 1: #large
		if [1,2,3,4,5] == sortedArray or [2,3,4,5,6] == sortedArray:
			return sum(dice)
	else: #type = 0, small 
		if all(x in sortedArray for x in [1,2,3,4]) or all(x in sortedArray for x in [2,3,4,5]) or all(x in sortedArray for x in [3,4,5,6]):
			return sum(dice)
	return 0

def removeTakenOptions():
	keysToPop = []
	#Gather all zeros first
	for key, value in allValues.items():
		value =  int(value)
		if value == 0 and "Pass" not in key:
			keysToPop.append(key)
	#Gather already taken choices
	global allKeysTaken
	for key in allKeysTaken:
		for keys, values in list(allValues.items()):
			values = int(values)
			print("or here")
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
for turns in range(10):
	print("Turn %s started.\n" %(turns + 1))
	dice = roll()
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
                     "Chance        " : sum(dice),
                     "Pass          " : 0}
	removeTakenOptions()
	choosePoints()
	print("\nTurn", turns + 1, "completed.")

print("Game Over! Your score was: " + str(scoreOfPlayer))



