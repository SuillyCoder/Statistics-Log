import numpy as np
from matplotlib import pyplot as plt
import math

#Let the user enter a number

number = 1
const = number

#Prepare different arrays for the different notations

one, logn, n, nlogn, squared, cube, exponent, factorial = [],[],[],[],[],[],[],[]
complexities = ["Factorial", "Exponential", "Cubic", "Quadratic", "Linearithmetic", "Linear", "Logarithmic", "Constant"]

def factorialNum(number):
    if number == 0:
        return 1
    else:
        return number * factorialNum(number - 1)

for x in range (3): 

    #Perform one operation at a time for the number
    #Append to corresponding array

    factorial.append(factorialNum(number))
    exponent.append(2**number)
    cube.append(number**3)
    squared.append(number**2)
    nlogn.append(number * (math.log(number)))
    n.append(number)
    logn.append(math.log(number))
    one.append(1)
    number += const

#Plot it out

plt.title("Algorithm Time Complexities", fontsize = 20)
plt.plot(n, factorial)
plt.plot(n, exponent)
plt.plot(n, cube)
plt.plot(n, squared)
plt.plot(n, nlogn)
plt.plot(n, n)
plt.plot(n, logn)
plt.plot(n, one)

plt.legend(complexities)
plt.xlabel("Data Input")
plt.ylabel("Time")
plt.show()
