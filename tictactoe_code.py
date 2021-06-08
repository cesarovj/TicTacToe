import random

# display a board game
def display_board(board):
    print('\n'*25)
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[7]+"|"+board[8]+"|"+board[9])

# accepting user input
def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, would you like to be X or O? ').upper()

    if marker == 'X':
        return ('O','X')
    else:
        return ('X','O')

# places your marker at certain position on the board
def place_marker(board, marker, position):

    board[position] = marker

# checks to see if that position mark won you the game
def win_check(board, mark):
    # Win Tic Tac Toe?

    # checks if all rows, all columns, or 2 diagonals all share same marker
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[6] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark))

# randomly decide what player goes first
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# checks if space on board is available
def space_check(board, position):
    
    # checks if there is a position with an empty string
    return board[position] == ' '

# checks if board is full
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    # board is full if returns True
    return True

# ask for players next choice
def player_choice(board):
    
    position = 0

    while position not in range(0,10) or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
    
    return position

# ask if want to play again
def replay():

    response = input('Would you like to play again? Y or N? ').upper()
    
    return response == 'Y'

# start of the game
print('Welcome to Tic Tac Toe!')

# while loop to keep running the game
while True:

    # Setup (Board, Who's first, Choose marker)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N? ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # Gameplay
    while game_on:
        if turn == 'Player 1':
            # shows the board
            display_board(the_board)
            # choose a postion
            position = player_choice(the_board)
            # place marker on position
            place_marker(the_board,player1_marker,position)
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            # check if tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game.')
                    game_on = False
                # next players turn
                else:
                    turn = 'Player 2'

        else:
            # shows the board
            display_board(the_board)
            # choose a postion
            position = player_choice(the_board)
            # place marker on position
            place_marker(the_board,player2_marker,position)
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            # check if tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game.')
                    game_on = False
                # next players turn
                else:
                    turn = 'Player 1'

    if not replay():
        break
