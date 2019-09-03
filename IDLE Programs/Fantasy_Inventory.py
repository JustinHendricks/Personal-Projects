#Code written 8/23/19
#Automate the Boring Stuff / Chapter 5 / Practice Problem 1: Fantasy Game Inventory
    #Note, lines 4, 6-8, and 12 given by the book

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} #Creates the dictionary that will be used as an inventory

def displayInventory(inventory): #Creates function to display inventory
    print("Inventory:") 
    item_total = 0 #Will be used to count how many items are in your inventory
    for k, v in inventory.items(): #Goes through each pair of a key and value
        print(str(v) + ' ' + k) #Prints the amount of the item fllowed by its names
        item_total += v #Adds the value, or amount of an item, to the total item count
    print("Total number of items: " + str(item_total)) #Prints the total item count

#Automate the Boring Stuff / Chapter 5 / Practice Problem 2: 
    #Note lines 16, and 30-33 given by book
    
def addToInventory(inventory, addedItems): #Creates function to display inventory
    global new_inventory #Defines new_inventory
    for i in addedItems: #Goes through the list of added items
        print(i) #Prints each item
        if i in inventory.keys(): #Checks if the item is already in your inventory
            inventory[i] += 1 #If it is, it will add 1 to its value
        else:
            inventory[i] = 1 #If not it will create a new key with a value of 1
    print('ITEMS ADDED') 
    new_inventory = inventory #Couldn't get it to run using inv, in order to see the new inventory you have to display 'new_inventory'
    

    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(new_inventory)
