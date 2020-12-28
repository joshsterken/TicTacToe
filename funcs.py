import random

# display the board
def display_board(board):
    print(str(board[7]) + '|' + str(board[8]) + '|' + str(board[9]))
    print('-----')
    print(str(board[4]) + '|' + str(board[5]) + '|' + str(board[6]))
    print('-----')
    print(str(board[1]) + '|' + str(board[2]) + '|' + str(board[3]))

# get play from player and update board
def get_move():
    letter = input("X or O")
    pos = int(input("Enter 1 - 9 to make a move."))
    return (letter, pos)

# update board
def update_board(board, letter, pos):
    board[pos] = letter

# check for win conditions
def is_winner(board, letter):
    return board[7] == board[5] == board[3] == letter or \
    board[1] == board[2] == board[3] == letter or \
    board[4] == board[5] == board[6] == letter or \
    board[7] == board[8] == board[9] == letter or \
    board[1] == board[4] == board[7] == letter or \
    board[2] == board[5] == board[8] == letter or \
    board[3] == board[6] == board[9] == letter or \
    board[1] == board[5] == board[9] == letter

# see who goes first
def who_first():
    guess = input("Player 1, heads or tails?")

    x = random.randint(1,2)

    if guess == 'heads':
        guess = 1
    else:
        guess = 2

    if x == guess:
        print('Player 1 goes first!')
        return 'player1'
    else:
        print('Player 2 goes first!')
        return 'player2'

def isBoardFull(board):
    return board.count(' ') == 1

def fresh_board():
    board = [' ' for x in range(10)]
    return board