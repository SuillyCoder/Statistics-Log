import numpy as np
from matplotlib import pyplot as plt

#Ask the user what temperature unit they want to display in

tempAve = None
tempUnit = None
availableTemps = ["C", "c", "F", "f", "K", "k"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while tempUnit not in availableTemps: 
    print("\nAvailable Temperature Units: \n\n[C]-Celcius\n[F]-Fahrenheit\n[K]-Kelvin")
    tempUnit = input("Please indicate the unit of temperature: ")

#If else statement on the temperature chosen

if tempUnit == "C" or tempUnit == "c":
    tempAve = 30
elif tempUnit == "F" or tempUnit == "f":
    tempAve = 86
elif tempUnit == "K" or tempUnit == "k":
    tempAve = 300

temperatures = np.round(np.random.normal(tempAve,3,12),2)

#Print out the details of the temperature records (such as average and standard deviation (or smth like that) )

print("Average Temperature is: " + str(np.mean(temperatures)))
print("The highest recorded temperature is: " + str(np.max(temperatures)))
print("The lowest recorded temperature is: " + str(np.min(temperatures)))
print("Temperature records are usually " + str(np.std(temperatures)) + " degrees " + tempUnit + " apart")

#Plot out the line graph of the monthly temperature reads

plt.title("Annual Temperature Report", fontsize = 20)
plt.plot(months,temperatures)
plt.xlabel("Months", fontsize=15)
plt.ylabel("Temperature Records", fontsize=15)
plt.grid()
plt.show()