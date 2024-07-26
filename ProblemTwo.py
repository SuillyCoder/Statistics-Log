import numpy as np
from matplotlib import pyplot as plt
import random

#Simulate the coin flipping by generating a random seed by 1 and 0.

heads,tails = [],[]
testRuns = []
headCount, tailCount, headSum, tailSum = 0,0,0,0
testCount, runCount = 10,10
#For at least X Times, do: 
    #Go through a single run of flipping a coin 10 times
    #Record the number of heads and the number of tails. 
    #Place them in an array
for x in range(testCount):
    for y in range (runCount):
        coinFlipper = random.randint(0,1)
        if coinFlipper == 1:
            print(coinFlipper)
            headCount += 1
            print("Headcount: " + str(headCount))
        else:
            print(coinFlipper)
            tailCount += 1
            print("Tailcount: " + str(tailCount))
    heads.append(headCount)
    tails.append(tailCount)
    headSum += headCount
    tailCount += tailCount
    testRuns.append("Test " + str(x+1))
    headCount, tailCount = 0,0


#Calculate the probability of heads and tails (preferrably with an accumulative variable)
print(heads)
print(tails)

headProb = ((headSum / (testCount * runCount)) * 100)
print("The coin landed on heads " + str(headProb) + "% of the time...")
print("...while the coin landed on tails " + str(100 - headProb) + "% of the time.")
print("Please view the bar graph for better visualization")

#Visualize the results via the bar graph
plt.title("Coin Toss Simulation")
plt.plot(testRuns,heads)
plt.plot(testRuns,tails)
plt.legend(["Heads", "Tails"])
plt.show()