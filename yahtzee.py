import random

scoreOfPlayer = 0

def roll():
    firstroll = rolldie(5)
    print("Your first roll was:", firstroll)
    result = input("Are you going to keep all or keep some? (k or r)")

    firsttime = 1
    keeping = []
    finalroll = []
    indexesused = []
    times = 0

    if result == "r":
        for times in range(2):
            if firsttime == 1:
                finalroll = firstroll
            else:
                print("Your current dice are:", finalroll)
                keepreplacing = input("Do you want to keep these dice (y or n)")
                if keepreplacing == "y":
                    break;
            index = 0
            while True:
                index = input("Type which one in the array of what you want to keep one at a time (q to stop)")
                if index == "q" or index == "Q":
                    break;  
                index = int(index) 
                while index in indexesused:                
                    index = input("Try another index. You are already replacing", finalroll[index - 1])
                    index = int(index)
                onetokeep = finalroll[index - 1]
                keeping.append(onetokeep)
                indexesused.append(index)
                print(onetokeep, "was stored.")
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
    	print("You have changed dice three times.")
    print("Your roll was: %s" %(finalroll))
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
	print(allValues)
	option = input("Here are all of your options to pick from. Choose which one you would like by entering the name of the option.")
	for key in allValues.iteritems():
		keycopy = lower(strip(key))
		option = lower(strip(option))
		if keycopy == option:
			scoreOfPlayer = scoreOfPlayer + int(allValues[key])
	print("Player Score: %s" %(scoreOfPlayer))

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
def checkStraight(type, dice):
	sortedArray = list(set(dice))
	sortedArray.sort(reverse=True)
	if type == 1: #large
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
	allValues = {"Aces" : countDice(1, dice), "Twos" : countDice(2, dice), "Three" : countDice(3, dice), "Four" : countDice(4, dice), "Five" : countDice(5, dice), "Six" : countDice(6, dice), "3 of a kind" : ofAKind(3, dice), "4 of a kind" : ofAKind(4, dice), "Full House" : checkFullHouse(dice), "Small Straight" : checkStraight(0, dice), "Large Straight" : checkStraight(1, dice), "Yahtzee" : ofAKind(5, dice), "Chance" : sum(dice)}
	choosePoints(dice)
	print("\nTurn", turns + 1, "completed.")



