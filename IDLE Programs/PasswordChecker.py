#Code written 8/24/19, Heavily edited 9/3/19
#Automate the Boring Stuff / Chapter 7 / Practice Problem 1: Strong Password Detection

#Expansion Ideas: add function that uses passwordChecker to try randomly generated passwords and print succesful ones as suggestions
import random, string #Libraries are used to generate test passwords. Not needed if yo are just using inputs.
run = 0 #Used to control the number of suggested passwords
def passwordChecker(password):
    checkr = {'length': False, 'uppercase': False, 'lowercase': False, 'digit': False} #Used to show what conditions need to be met for password to be secure
    if len(password) >= 8: #Checks to see if the length of the password is at leats 8 characters
        checkr['length'] = True #Checks length condition as true
    for i in password: #Goes through every charcter in the password
        if i.isupper() == True:
            checkr['uppercase'] = True #If the character is uppercase, its passed as True
        if i.islower() == True:
            checkr['lowercase'] = True #If the character is lowercase, its passed as True
        if i.isdigit() == True:
            checkr['digit'] = True #If the character is a digit, its passed as True
    for k, v in checkr.items():
       print(str(k) + ': ' + str(v)) #Printes the dictionary in order to show what conditions haven't been met
    if checkr['length'] == True and checkr['uppercase'] == True and checkr['lowercase'] == True and checkr['digit'] == True:
        print("Congrats! Your password is secure!") #If all conditions are met it tells you the password is secure
    else:
        print("Warning! The password you typed is not secure!")
        print("It is reccomended that your password is at least 8 characters long, and that you have at least 1 capital letter, 1 lowercase letter, and 1 digit")
        #If all conditions are not met, it prints out the conditions for a good password
        #Expansion Ideas: See which condition/s is/are false and print out what the password specifically needs
while run != 10: #Runs this 10 times
    lent = random.randint(1,12) #Picks a random number of characters for the password to have. This is to test length in checkr.
    password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(lent)]) #Makes the password a random series of letters and numbers
    print(password)
    passwordChecker(password) #Shows and checks the password
    run += 1 #Runs this loop again
