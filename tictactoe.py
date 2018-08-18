# Tic Tac Toe

import random


def draw_board(board):
    # This function prints out the board that it was passed

    # "board" is a list of 10 strings representing the board (index 0 ignored)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def input_player_letter():
    # Lets player type which letter they want to play as.
    # Returns the list with player's letter as the first item, and the CPU's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter, the second is the CPU's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose who goes first, player or CPU.
    if random.randint(0, 1) == 0:
        return 'CPU'
    else:
        return 'player'


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # bo = board        le = letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def get_board_copy(board):
    # make a duplicate of board list and return the duplicate
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ''


def get_player_move(board):
    # Let the player type in their move.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()  # need to figure out how to allow player to only have to insert an integer, instead of '#'
    return int(move)


def choose_random_move_from_list(board, moves_list):
    # returns a valid move from the passed list on the passed board.
    # returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Tic Tac Toe AI------------------------
    # First: check if I can win in next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Second: check if the player could win on their next move, and block them
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Third: try taking one of the corners, if available.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Fourth: try to take the center, if available.
    if is_space_free(board, 5):
        return 5

    # Fifth: move on one of the sides, left or right.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    # return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Ello Govna, welcome to Tic Tac Toe!!!!')

while True:
    # Reset the board
    the_board = ['']*10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn.
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Woopty-doo Bazzle, you won!!!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ouch.... tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # CPU's turn.
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('Muahahahaha the CPU has beaten you!! Lose, you have!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('Ouch.... tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
