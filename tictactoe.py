import funcs as f

def main():
    # create board
    board = f.fresh_board()

    while not f.isBoardFull(board):

        f.display_board(board)

        letter, pos = f.get_move()

        f.update_board(board, letter, pos)

        if f.is_winner(board, letter):
            
            f.display_board(board)
            print(f'{letter} wins!!')
            input('Hit any key to continue...')
            break
    if input('Would you like to play again (y/n)? ') == 'y':
        board = f.fresh_board()
        main()
    else:
        quit()

# welcome
print("Welcome to TicTacToe!")

# commence play
main()

# ask to play again