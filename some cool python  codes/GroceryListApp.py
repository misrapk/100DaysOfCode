#Grocery Billing List APp
import datetime

#TODO: Welcome message with current time 
print("\nWelcome to the Grocery List App.")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print("Current Date and Time : {}/{} \t {}:{}".format(day, month, hour, minute))


GroceryList = ['Vegetables', 'Biscuit']

print("\nYou currently have {} and {} in your list.".format(GroceryList[0], GroceryList[1]))


#TODO: user INput
item = input("Add item in your Grocery List: ")
GroceryList.append(item.title())
item = input("Add item in your Grocery List: ")
GroceryList.append(item.title())
item = input("Add item in your Grocery List: ")
GroceryList.append(item.title())

print("\nHere Your Grocery List: ")
print(GroceryList)

#TODO: sort the list
GroceryList.sort()
print("Here is your grocery list sorted: ")
print(GroceryList)

#TODO: Simulating Grocery Shopping
print("\nSimulating Grocery Shopping....")
print("\nCurrent Grocery List: {} items.".format(len(GroceryList)))
print(GroceryList)


#TODO: removed the buy item 
buyItem = input("What item did you just buy: ").title()
GroceryList.remove(buyItem)
print("Removing {} from the list...".format(buyItem))

print("\nCurrent Grocery List: {} items.".format(len(GroceryList)))
print(GroceryList)
buyItem = input("What item did you just buy: ").title()
GroceryList.remove(buyItem)
print("Removing {} from the list...".format(buyItem))

print("\nCurrent Grocery List: {} items.".format(len(GroceryList)))
print(GroceryList)
buyItem = input("What item did you just buy: ").title()
GroceryList.remove(buyItem)
print("Removing {} from the list...".format(buyItem))

#TODO: final WOrk
print("\nCurrent List: {} items.".format(len(GroceryList)))
print(GroceryList)

noItem = GroceryList.pop()
print("\nSorry, the store is out of {}.".format(noItem))

newItem = input("What item would you like instead: ").title()
GroceryList.insert(0, newItem)


print("Here is your Final List: ")
print(GroceryList)