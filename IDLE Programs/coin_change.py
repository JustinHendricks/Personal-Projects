import random
def num_coins(cents):
    change = {'quarter': 0, 'dime': 0, 'nickel' : 0, 'penny': 0}
    num_coins = 0
    change_given = 0
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
