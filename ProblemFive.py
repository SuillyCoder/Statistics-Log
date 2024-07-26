import numpy as np
from matplotlib import pyplot as plt
import random
#Set up the two dice's roll history

dice = ["Dice One", "Dice Two", "Dice Three", "Dice Four", "Dice Five"]
diceOne_Rolls = []
diceTwo_Rolls = []
diceThree_Rolls = []
diceFour_Rolls = []
diceFive_Rolls = []
testRuns, rollSums = [], []


#Ask how many tests to conduct

runs = int(input("How many trials would you like to run?: "))

#For X amount of tests:
for x in range(runs):
    diceOne_Rolls.append(random.randint(1,6))
    diceTwo_Rolls.append(random.randint(1,6))
    diceThree_Rolls.append(random.randint(1,6))
    diceFour_Rolls.append(random.randint(1,6))
    diceFive_Rolls.append(random.randint(1,6))
    testRuns.append("Run " + str(x+1))

#Calculate the dice with the highest rollCount
rollSums.append(np.sum(diceOne_Rolls))
rollSums.append(np.sum(diceTwo_Rolls))
rollSums.append(np.sum(diceThree_Rolls))
rollSums.append(np.sum(diceFour_Rolls))
rollSums.append(np.sum(diceFive_Rolls))

maxDiceRolls = np.max(rollSums)
minDiceRolls = np.min(rollSums)

#Prepare the line graph

plt.plot(testRuns, diceOne_Rolls)
plt.plot(testRuns, diceTwo_Rolls)
plt.plot(testRuns, diceThree_Rolls)
plt.plot(testRuns, diceFour_Rolls)
plt.plot(testRuns, diceFive_Rolls)
plt.legend(dice)

plt.text(0.5,6,"The dice with the highest roll count is: " + dice[rollSums.index(maxDiceRolls)])
plt.text(0.5,5.5,"The dice with the lowest roll count is: " + dice[rollSums.index(minDiceRolls)])
plt.title("Dice Simulation Test")
plt.xlabel("Number of Runs")
plt.ylabel("Number Landed")

#Display the results
plt.show()


