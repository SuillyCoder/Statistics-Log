import numpy as np
from matplotlib import pyplot as plt

#Endlessly ask the user for product info until they decide not to

addMore = "Y"
itemList, saleList = [],[]
while addMore == "Y" or addMore == "y":
    item = input("Enter an item: ")
    sale = int(input("Enter its generated revenue: "))
    itemList.append(item)
    saleList.append(sale)
    addMore = input("Would you like to add another item entry? [Y/N]: ")
    if addMore != "Y" and addMore != "y" and addMore != "N" and addMore != "n":
          addMore = input("Please input a valid response Y/N: ")
    #Ask them for the product
    #Ask them for for the total generated revenue (in Pesos)
    #Add into an array (both item and price)
    #Do u wanna add more?
npSales = np.array(saleList)
#Indicate the smallest sale and the highest sale (item)

print("The item that generated the most revenue is: " + itemList[saleList.index(np.max(npSales))])
print("The item that generated the least revenue is: " + itemList[saleList.index(np.min(npSales))])
print("The total revenue generated by these items is: " + str(np.sum(saleList)))

#Indicate total number of sales for the range of items
#Plot the bar graph

plt.bar(itemList, saleList)
plt.title("Item Sales Record")
plt.xlabel("Generated Revenue", fontsize = 15)
plt.ylabel("Items", fontsize = 15)
plt.show()