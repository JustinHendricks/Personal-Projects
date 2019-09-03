#Code written 8/28/19
#Inspired by this video https://youtu.be/HWW-jA6YjHk?list=PLC260E5J31yEtHISBAAFdGn-TnbNCxPbC

#The idea behind solving this problem was inspired by another project in this repository 'fantasy inventory'. The program sees how much money is left and distributes change based on that, at the end it displays a tally of what coins you need to give exact change

def num_coins(cents):
    change = {'quarter': 0, 'dime': 0, 'nickel' : 0, 'penny': 0} #Creates dictionary to keep track of how many of each coin you need
    num_coins = 0 #Keeps track of how many coins you have in total
    change_given = 0 #Not neccassary, just to make sure your input matches the change give
#Each loop checks if cents(The amount of change left to give) is greater than the value of the coin(25, 10, etc.)
#While that is the case, the program subtracts that cents' value, adds the cents' value to 'change_given', and adds 1 to its dictionary value
    while int(cents) >= 25:
         cents = int(cents) - 25
         change['quarter'] += 1
         change_given += 25
    while int(cents) >= 10:
        cents -= 10
        change_given += 10
        change['dime'] += 1
    while int(cents) >= 5:
        cents -= 5
        change_given += 5
        change['nickel'] += 1
    while int(cents) >= 1:
        cents -= 1
        change_given += 1
        change['penny'] += 1
    print('Change:')
    for k, v in change.items():
        print(str(v), k)
        num_coins += v
    print(num_coins)
    print('Change given =', change_given)
    


num_coins(input()) 
