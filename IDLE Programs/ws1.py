import webbrowser, sys, pyperclip

def googletool():
    runagain = True
    run = True
    searcher = True
    while run == True:
        print("Welcome to googler, what would you like to do? (Type 'search' to google something, or 'map' to find directions to somewhere")
        print("To exit press enter")
        function = input()
        if function == 'search':
            print("Welcome to search! You can exit at any time by typing 'leave()'")
            print("Pressing enter will search whatever is on your clipboard!")
            search = input()
            if search == '':
                search = pyperclip.paste()
            while searcher == True:
                if search == 'leave()':
                    break
                    searcher = False
                if ' ' in search:
                    search = search.replace(' ', '+' )
                webbrowser.open('google.com/search?q=' + search)
                search = input()
        if function == 'map':
            while runagain == True:
                print("Welcome to map!")
                print("Pressing enter will map whatever is on your clipboard!")
                print("Would you like to display a location or directions?")
                answ = input()
                if answ == 'directions':
                    print("Where are you traveling from?")
                    start = input()
                    if start == '':
                        start = pyperclip.paste()
                    print("Okay, and where are you going")
                    end = input()
                    if end == '':
                        end = pyperclip.paste()
                    if ' ' in start:
                        start = start.replace(' ', '+')
                    if ' ' in end:
                        end = end.replace(' ', '+')
                    webbrowser.open('google.com/maps/dir/' + start + '/' + end)
                if answ == 'location':
                    print("Where would you like to see?")
                    loc = input()
                    if loc == '':
                        loc = pyperclip.paste()
                    if ' ' in loc:
                        loc = loc.replace(' ', '+')
                    webbrowser.open('google.com/maps/place/' + loc)
                print("Would you like to map something else?")
                answ = input()
                if answ == 'yes':
                   runagain = True
                if answ == 'no':
                    runagain = False
        if function == '':
            run = False
                

googletool()
