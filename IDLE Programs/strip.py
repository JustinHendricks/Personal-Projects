#Code written 8/29/19
#Automate the Boring Stuff / Chapter 7 / Practice Problem 2: Regex Version of strip()
def strip():
    print("Type string that you will strip")
    string = input()
    print("Type character/s you wish to remove")
    char = input()
    print(string.replace(char, ''))
#Code is self explanitory, it finds the character/s you want to remove in the string you typed and prints the new string
