import random
scoreOfPlayer = 0
def roll():
    firstroll = rolldie(5)
    print("Your first roll was:", firstroll, "\n")
    result = input("Are you going to keep all or keep some? (k or r) ")
    result = (result.lower()).strip()
    firsttime = 1
    keeping = []
    finalroll = []
    indexesused = []
    times = 0
    brokerule = False
    
    if result == "r":
        for times in range(2):
            if firsttime == 1:
                finalroll = firstroll
            else:
                print("Your current dice are:", finalroll)
                result = input("Do you want to keep these dice (y or n)? ")
                result = (result.lower()).strip()
                if result == "y":
                    break;
                elif result != "n":
                    print("I'll take that as a no.\n")
            index = 0
            while True:
                index = input("Type which one in the array of what you want to keep one at a time (q to stop) ")
                index = (index.lower()).strip()
                if index == "q":
                    break;  
                try:
                    index = int(index)
                    while index in indexesused:                
                        print("Sorry, you are already replacing", finalroll[index - 1], ".\n")
                        index = input("Try another index. ")
                        index = int(index)   
                    onetokeep = finalroll[index - 1]
                    keeping.append(onetokeep)
                    indexesused.append(index)
                    print("You are keeping " + str(onetokeep) + "\n")
                except IndexError:
                    print("\nYou only have 5 dice!\n")
                    continue
                except:
                    print("\nStop trying to break the rules!\n")
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
            firsttime = 0
    else:
        finalroll = firstroll
    if times == 2:
    	print("You have changed some dice three times.")
    print("Your roll was: %s\n" %(finalroll))
    return finalroll

def rolldie(numToRoll):
    diechoices = ['1', '2', '3', '4', '5', '6']
    result = []
    for x in range(numToRoll):
        result.append(int(random.choice(diechoices)))
    return result

def countDice(number, dice):
	counter = 0
	for n in dice:
		if n == number:
			counter = counter + 1
	score = counter * number
	return score

def choosePoints(dice):
    for key, value in allValues.items():
        key = str(key)
        value = str(value)
        print(key + ":\t" + value + " points.")
    global scoreOfPlayer
    option = input("\nHere are all of your options to pick from. Choose which one you would like by entering the name of the option.\n")
    for key, value in allValues.items():
        keycopy = (key.strip()).lower()
        option = (key.strip()).lower()
        if keycopy == option:
            scoreOfPlayer = scoreOfPlayer + int(value)
            print("Player Score: %s\n" %(scoreOfPlayer))
            #Still figuring out how to remove an entry in dictionary
            return;

def checkFullHouse(dice):
	for num in dice:
		if dice.count(num) == 3:
			for second_num in dice:
				if dice.count(second_num) == 2:
					return 25
	return 0

def ofAKind(numOfKind, dice):
	for number in dice:
		if dice.count(number) == numOfKind:
			if numOfKind == 5:
				return 50
			else:
				return numOfKind * number
	return 0
def checkStraight(smallOrLarge, dice):
	sortedArray = list(set(dice))
	sortedArray.sort(reverse=True)
	if smallOrLarge == 1: #large
		if sum(sortedArray) == 15:
			return sum(dice)
	else: #type = 0, small
		if sum(sortedArray) > 10:
			sortedArray.remove(sortedArray[0])
			if sum(sortedArray) == 10:
				return sum(dice)
	return 0

for turns in range(10):
	print("Turn %s started.\n" %(turns + 1))
	dice = roll()
	allValues = {"Aces          " : countDice(1, dice),
                     "Twos          " : countDice(2, dice),
                     "Three         " : countDice(3, dice),
                     "Four          " : countDice(4, dice),
                     "Five          " : countDice(5, dice),
                     "Six           " : countDice(6, dice),
                     "3 of a kind   " : ofAKind(3, dice),
                     "4 of a kind   " : ofAKind(4, dice),
                     "Full House    " : checkFullHouse(dice),
                     "Small Straight" : checkStraight(0, dice),
                     "Large Straight" : checkStraight(1, dice),
                     "Yahtzee       " : ofAKind(5, dice),
                     "Chance        " : sum(dice)}
	choosePoints(dice)
	print("\nTurn", turns + 1, "completed.")



