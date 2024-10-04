#Lists
# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Mocha"
# ]
# print(coffee_order[2]) #Prints the item
# coffee_order[2] = "Charlie - Hot Chocolate" #allows for updating an item on the list
# coffee_order.append("Diane - Cappucino") #allows for adding an item to the end of the list
# print(coffee_order) 
# print(len(coffee_order)) #Counts the items on the list
#.remove(), .reverse(), .sort(), .count(), .extend()
# -------------------------------------------------------------------------
#Activity 1 - 
# -------------------------------------------------------------------------
#Dictionaries
# animals = {
#     "Lion" : "Cub",
#     "Pigeon" : "Squab",
#     "Gecko" : "Baby Gecko",
#     "Hedgehog" : "Hoglet"
# }
# animals["Gecko"] = "Hatchling" #Updates item in the dictionary
# print (animals["Gecko"])
# print(animals.keys()) #returns a list of the keys within the dictionary
# print(animals.values()) #returns a list of the values within the dictionary
# print(animals.items()) #returns a list of the key:value pairs
# print(animals.get("Gecko")) #Finds the value of a key. will return none if the key does not exist. A custom error message if a key can't be found. .get helps avoid code-stopping errors.
# print(animals.setdefault("Lion", "Baby Lion")) #Takes a key and a value. If the key exists, it will return with its current value. 
# animals.setdefault("Zebra", "Foal") #If the key doesn't exist, it will be added to the dictionary with the value specified.
# animals.update({"Fish" : "Fry", "Crab" : "Zoea"}) #Merges two dictionaries into one.
# animals.pop("Lion") #Specify the key of the item that wants removing. Can be used to remove the last item.
# -------------------------------------------------------------------------
#Activity 1 - Create a list of your three favorite websites and then add another using a method.
# fav_website = [
#     "Youtube",
#     "Google",
#     "Pinterest"
# ]
# fav_website.append("Spotify")
# fav_website.append("Etsy")
# fav_website.pop()
# print(fav_website)
# -------------------------------------------------------------------------
#Activity 2 - Reseearch into the following list of methods:.remove(),.reverse(),.sort(),.count(),.extend()
fizzy_pop = [
    "Pepsi",
    "Coca-Cola",
    "Fanta Orange",
    "Mountain Dew"
]
# fizzy_pop.remove("Pepsi") #Removes an item with a specified value.
# fizzy_pop.reverse() #Reverses the list.
# fizzy_pop.sort() #sorts the list in alphabetical order
# fizzy_pop.count() 
fizzy_pop.extend("Pepsi")
print(fizzy_pop) 