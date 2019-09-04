#Code written 8/11/19
#Automate the Boring Stuff / Chapter 3 / Practice Problem 1: The Collatz Sequence

run = True
def collatz(number):
   while number != 1: #Runs function until number == 1
        if number % 2 != 0: #Checks if number is odd
            number = number * 3 + 1
            print (number)
            number = number / 2
            print (number)
        if number % 2 == 0: #Checks if number is even
            number = number / 2
            print (number)
    print('done')
print('Enter number')
while run == True:
    try:
        number = int(input())
        collatz(number)
        run = False
    except ValueError:
        print('Please enter a number') #Prevents user from inputting a string
