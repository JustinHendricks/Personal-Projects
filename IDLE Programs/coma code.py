#Code written 8/23/19
#Automate the Boring Stuff / Chapter 4 / Practice Problem 1: Comma Code

def commas(list): #Function designed to take a list of strings, return said list as a string with items being separated by a comma
    seperator = ', ' #Added to each item in the lis
    ender = 'and ' #Added before the last item in the list
    i = 0
    sentence = [] #Used to create a new list with edited items
    com_str = "" #What will be printed to get the string with commas
    while i < len(list):
        if i < len(list) - 1:
            word = list[i] + seperator #If i is not on the last index of the list, it will add a comma and a space
        if i == len(list) - 1:
            word = ender + list[i]  #If it is on the last index of the list, it will add 'and ' before the word
        sentence.append(word) #The altered item gets added to the list
        i += 1
    i = 0
    while i < len(list):
        com_str += sentence[i] #Each of the new words in the new list is added to to the string
        i += 1
    print(com_str) #Prints out the items now with commas


