run = True
def collatz(number):
    while number % 2 != 0:
        number = number * 3 + 1
        print (number)
        number = number / 2
        print (number)
    while number % 2 == 0:
        number = number / 2
        print (number)
    if number == 1:
        print('done')
print('pick a number')
while run == True:
    try:
        number = int(input())
        collatz(number)
        run = False
    except ValueError:
        print('Please enter a number')
    
