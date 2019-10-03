import random
global winner

board = [
        [ ' ' , ' ' , ' '],
        [ ' ' , ' ' , ' '],
        [ ' ' , ' ' , ' ']
        ]
spaces_available = [ 11, 12, 13, 21, 22, 23, 31, 32, 33]



def board_maker(list_of_lists):
    i = 0
    for l in list_of_lists:
        print(l)
        print("")


def player_turn(symbol):
    while True:
        player_row = input( symbol + ", input your row: ")
        player_column = input( symbol + ", input your column: ")
        if board[int(player_row) - 1][int(player_column) - 1] != ' ':
            print("Your opponent has already marked that spot.")
        else:
            mark = int((player_row) + (player_column))
            if mark in spaces_available:
                spaces_available.remove(mark)
            board[int(player_row) - 1][int(player_column) - 1] = symbol
            break

def cpu_turn(symbol):
    if len(spaces_available) >= 1:
        spot = random.choice(spaces_available)
        spaces_available.remove(spot)
        row = (spot // 10) - 1
        column = (spot % 10) - 1
        board[row][column] = symbol
    else :
        pass
    

def win_row(): #checks if a player has gotten three in a horizontal row
    global winner
    in_a_row = 1
    for r in range(len(board)):
        for s in range(len(board[r])):
            if s == 2:
                break
            if board[r][s] == board[r][s + 1] and board[r][s] !=  ' ':
                in_a_row += 1
            if in_a_row == 3:
                winner = board[r][s]
                return True         
        in_a_row = 1
def win_column():
    global winner
    in_a_row = 1
    r = 0
    c = 0
    while c < (len(board[r]) - 1):
        while r < (len(board) - 1):
            if board[r][c] == board[r + 1][c] and board[r][c] != ' ':
                in_a_row += 1
            if in_a_row == 3:
                winner = board[r][c]
                in_a_row = 0
                return True
            r += 1
        r = 0
        c += 1
        in_a_row = 1

def win_diagonal():
    global winner
    in_a_row = 1
    r = 0
    c = 0
    if board[r][c] == board[r + 1][c + 1]:
        while r < (len(board) - 1):
            if board[r][c] == board[r + 1][c + 1] and board[r][c] != ' ':
                in_a_row += 1
            print(in_a_row)
            if in_a_row == 3:
                winner = board[r][c]
                in_a_row = 0
                return True
            r += 1
            c += 1
            
    else:
        r = 2
        c = 0
        in_a_row = 1
        if board[r][c] == board[r - 1][c + 1]:
            while c < (len(board[r]) - 1):
                if board[r][c] == board[r - 1][c + 1] and board[r][c] != ' ':
                    in_a_row += 1
                if in_a_row == 3:
                    winner = board[r][c]
                    in_a_row = 0
                    return True
                r -= 1
                c += 1
        
def win_conditions():
    row = win_row()
    column = win_column()
    diagonal = win_diagonal()
    if row == True or column == True or diagonal == True:
        return True
    elif len(spaces_available) < 1:
        return 'tie'

def reset(spaces):
    for r in range(len(board)):
                for c in range(len(board[r])):
                    board[r][c] = ' '
    space_reset = [ 11, 12, 13, 21, 22, 23, 31, 32, 33]
    for i in space_reset:
        spaces.append(i)

def pvp():
    p1_name = input("Player 1, what is your name? ")
    p2_name = input("Player 2, what is your name? ")
    p1_symbol = input("Player 1's Symbol: ")
    p2_symbol = input("Player 2's Symbol: ")
    print(board_maker(board))
    while True:
        player_turn(p1_symbol)   
        print(board_maker(board))
        has_won = win_conditions()
        player_turn(p2_symbol)
        print(board_maker(board))
        has_won = win_conditions()
        if has_won == True:
            print( winner + " has won the game!!")
            break
        
def single_player():
    p1_symbol = input("What is your symbol?")
    print("The CPU's symbol is 'CPU'")
    print(board_maker(board))
    while True:
        player_turn(p1_symbol)   
        print(board_maker(board))
        has_won = win_conditions()
        cpu_turn(CPU)
        print(board_maker(board))
        has_won = win_conditions()
        if has_won == True:
            print( winner + " has won the game!!")
            break

def cpu_vs_cpu():
    print(board_maker(board))
    while True:
        cpu_turn('X')   
        print(board_maker(board))
        has_won = win_conditions()
        cpu_turn('O')
        print(board_maker(board))
        has_won = win_conditions()
        if has_won == True:
            print( winner + " has won the game!!")
            break
        elif has_won == 'tie':
            print("The game has ended in a tie.")
            break

print("Welcome to Tic Tac Toe!")
mode = input("Type 'single' to play against the CPU, 'pvp' to play against a friend and 'watch' to see CPU vs CPU: ")
if mode == 'single':
    single_player()
    while True:
        runnit = input("Do you want play again? ")
        if runnit == 'yes':
            for r in board:
                for c in board[r]:
                    c = ' '
            single_player()
        if runnit == 'no':
            break
elif mode == 'pvp':
    pvp()
    while True:
        runnit = input("Do you want play again? ")
        if runnit == 'yes':
            for r in board:
                for c in board[r]:
                    c = ' '
            pvp()
        if runnit == 'no':
            break
elif mode == 'watch':
    cpu_vs_cpu()
    while True:
        runnit = input("Do you want play again? ")
        if runnit == 'yes':
            reset(spaces_available)
            cpu_vs_cpu()
        if runnit == 'no':
            break
