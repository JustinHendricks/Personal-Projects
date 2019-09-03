tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(list):
    x = 0
    i = 0
    k = 0
    indent = ' '
    strs = ''
    seperator = ' '
    strs = ''
    while k < len(list[0]): #Goes through items contained in first list
        while i < len(list): #Goes through first/second/.. item in each list
            strs += list[i][k] + seperator #Creates a 'sentence' of all the items in a line with spaces in between
            i = i + 1 #What moves through each list
        if len(strs) < 20: #Checks length of strs
            repeater = 20 - len(strs) #Creates number that will determine indentation
            while x < repeater: #Creates length of indentation
                indent += " "
                x += 1
            line = indent + strs #Spaces in front of strings(strs) + strings(strs) = right aligned
        else:
            line = strs #If the length of the line is 20 it will just use the strs
        print(line)
        x = 0
        i = 0
        k += 1
        indent = ' '
        strs = ''
        seperator = ' '
        strs = ''
        # ^^ Resets variables to make another line
        #Ways to improve: Create left align, create a seperate function that sees which line is longest and uses that instead of 20

printTable(tableData)
