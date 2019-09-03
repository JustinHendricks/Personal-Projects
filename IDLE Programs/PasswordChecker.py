import random
import string
run = 0
def passwordChecker(password):
    checkr = {'length': False, 'uppercase': False, 'lowercase': False, 'digit': False}
    score = 0
    upcheck = 0
    lowcheck = 0
    digcheck = 0
    if len(password) >= 8:
        checkr['length'] = True
        score += 1
    for i in password:
        if i.isupper() == True:
            upcheck += 1
        if i.islower() == True:
            lowcheck += 1
        if i.isdigit() == True:
            digcheck += 1
    if upcheck > 0:
        checkr['uppercase'] = True
        score += 1
    if lowcheck > 0:
        checkr['lowercase'] = True
        score += 1
    if digcheck > 0:
        checkr['digit'] = True
        score += 1
    for k, v in checkr.items():
       print(str(k) + ': ' + str(v))
    if score == 4:
        print("Congrats! Your password is secure!")
    else:
        print("Warning! The password you typed is not secure!")
        print("It is reccomended that your password is at least 8 characters long, and that you have at least 1 capital letter, 1 lowercase letter, and 1 digit")

while run != 10:
    lent = random.randint(1,12)
    password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(lent)])
    print(password)
    passwordChecker(password)
    run += 1
