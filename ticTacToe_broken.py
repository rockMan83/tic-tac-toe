#### tic-tac-toe game ####
# To Do:


#Note: For future development, the issue with having to duplicate functions for one change has to do with all the
#personalization, such as using the players first name for each turn.

def initialize():  #Get player names and their characters
    global name1
    global name2
    global player1
    global player2
    global winner_name
    global loser_name
    name1 = winner_name = input('Hello Player 1.  What is your name?\n')
    player1 = input(f'\nHi {name1}. Do you want to be X or O?\n').upper()
    while player1 not in ('X', 'O'):
        player1 = input('\nDon\'t be cheeky.  X or O?\n').upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    name2 = loser_name = input('\nAnd hello Player 2.  What is your name?\n')
    print(f'\nNice to meet you {name1} and {name2}! {name1} chose {player1}, so {name2} will be {player2}.')
    print(f'\nOK. Let\'s play Tic-Tac-Toe! \n{name1} goes first.\n')


#def continueGame(board):
    ####  The loop only succeeded in checking row 1 and column 1.  I did not figure out why so I just wrote out all the conditions.  ####
#    for i in range(3):
#        for j in range(3):
#            if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]) or \
#                (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
#                return False
#            else:
#                return True


def cats_game(board):
    """Checks if the any of the values in the board list has not been used"""
    if board[0][0] == 1 or board[0][1] == 2 or board[0][2] == 3 or \
            board[1][0] == 4 or board[1][1] == 5 or board[1][2] == 6 or \
            board[2][0] == 7 or board[2][1] == 8 or board[2][2] == 9:
        return False
    else:
        return True


def tic_tac_toe(board):
    """Lazy function to check if 3 in a row is obtained"""
    if (board[0][0] == board[1][0]) and (board[0][0] == board[2][0]) or \
            (board[0][1] == board[1][1]) and (board[0][1] == board[2][1]) or \
            (board[0][2] == board[1][2]) and (board[0][2] == board[2][2]) or \
            (board[0][0] == board[0][1]) and (board[0][0] == board[0][2]) or \
            (board[1][0] == board[1][1]) and (board[1][0] == board[1][2]) or \
            (board[2][0] == board[2][1]) and (board[2][0] == board[2][2]) or \
            (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]) or \
            (board[0][2] == board[1][1]) and (board[0][2] == board[2][0]):
        return True
    else:
        return False


def p1_turn(board):
    draw_board(board)
    move1 = get_move_p1(board)
    update_board_p1(board, int(move1))
    return board


def p2_turn(board):
    draw_board(board)
    move2 = get_move_p2(board)
    update_board_p2(board, int(move2))
    return board


def p3_turn(board):
    draw_board(board)
    move3 = get_move_p3(board)
    update_board_p3(board, int(move3))
    return board


def draw_board(board):
    for i in range(3):
        line_to_draw = ''
        for j in range(3):
            line_to_draw += ' | ' + str(board[i][j])  # Need to convert board values to strings in order to append
        line_to_draw += ' | '
        print(line_to_draw)


def get_move_p1(a):
    move_p1 = input(f'\n{name1} ({player1}), please enter your move (1-9)\n')
    while move_p1 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        move_p1 = input(f'Come on {name1} ({player1}), enter a valid move (1-9)\n')
    # fancy for loop to check if position is already taken.  I still don't understand how it works exactly.
    while int(move_p1) not in (item for sublist in a for item in sublist):
        move_p1 = input('Space taken. Please choose another.\n')
    return move_p1


def get_move_p2(a):
    move_p2 = input(f'\n{name2} ({player2}), please enter your move (1-9)\n')
    while move_p2 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        move_p2 = input(f'Come on {name2} ({player2}), enter a valid move (1-9)\n')
    while int(move_p2) not in (item for sublist in a for item in sublist):
        move_p2 = input('Space taken. Please choose another.\n')
    return move_p2


def get_move_p3(a):
    move_p3 = input(f'\n{name3} ({player3}), please enter your move (1-9)\n')
    while move_p3 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        move_p3 = input(f'Come on {name3} ({player3}), enter a valid move (1-9)\n')
    while int(move_p3) not in (item for sublist in a for item in sublist):
        move_p3 = input('Space taken. Please choose another.\n')
    return move_p3


def update_board_p1(board, pos):
    """Convert/Interpret move into list index and replace with player character"""
    print('')  #Creates blank line
    pos -= 1    #Change pos to be a value between 0 - 8 since lists begin at 0
    row = pos // 3    #Integer divide by 3 to get the row number
    col = pos % 3    #Modulus gets the column number
    board[row][col] = player1


def update_board_p2(board, pos):
    print('')  #Creates blank line
    pos -= 1    #Change pos to be a value between 0 - 8 since lists begin at 0
    row = pos // 3    #Integer divide by 3 to get the row number
    col = pos % 3    #Modulus gets the column number
    board[row][col] = player2


def update_board_p3(board, pos):
    print('')  #Creates blank line
    pos -= 1    #Change pos to be a value between 0 - 8 since lists begin at 0
    row = pos // 3    #Integer divide by 3 to get the row number
    col = pos % 3    #Modulus gets the column number
    board[row][col] = player3


def play_again():
    global play
    global name3
    global player3
    global blah
    global winner_player
    global winner_name
    global loser_player
    global loser_name
    global game_over
    global p1_continue
    global p2_continue
    again = input('Would you like to play again? (type \'y\' or anything else to quit)\n').lower()
    if again in ('y', 'yes'):
        reset = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        rematch = input('Rematch? (type \'y\' or \'n\')\n').lower()
        if rematch in ('y', 'yes'):
            print(f'\nOne mo\' gain!\nWinner ({winner_name}) goes first.\n')
            blah = reset
            game_over = False
        else:
            name3 = input('\nNEW CHALLENGER!  What is your name?\n')
            winner_continue = input(f'\n{winner_name}, Do you want to continue? (type \'y\' or \'n\')\n').lower()
            if winner_continue in ('n', 'no'):
                winner_name = name3
                player3 = winner_player
                p1_continue = False
            else:
                loser_name = winner_name
                loser_player = winner_player
                winner_name = name3
                if loser_player == 'X':
                    player3 = 'O'
                else:
                    player3 = 'X'
            print(f'\nWelcome {name3}, you will be {player3}\n')
            game_over = False
            play = False
            blah = reset
    else:
        play = False
        p1_continue = False
        p2_continue = False


def do_round_p1vsp2(board):
    global p1_win
    global p1_loss
    global p2_win
    global p2_loss
    global winner_name
    global winner_player
    global loser_name
    global loser_player
    global game_over
    while not game_over:
        if winner_name == name1:
            p1_turn(board)
            if tic_tac_toe(board):
                p1_win += 1
                p2_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name1} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name1
                winner_player = player1
                loser_name = name2
                loser_player = player2
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            p2_turn(board)
            if tic_tac_toe(board):
                p2_win += 1
                p1_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name2} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
        else:
            p2_turn(board)
            if tic_tac_toe(board):
                p2_win += 1
                p1_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name2} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            p1_turn(board)
            if tic_tac_toe(board):
                p1_win += 1
                p2_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name1} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name1
                winner_player = player1
                loser_name = name2
                loser_player = player2
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name2} {str(p2_win)} wins, {str(p2_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name1
                loser_player = player1
                game_over = True
    play_again()


def do_round_p1vsp3(board):
    global p1_win
    global p1_loss
    global p3_win
    global p3_loss
    global winner_name
    global winner_player
    global loser_name
    global loser_player
    global game_over
    while not game_over:
        if winner_name == name1:
            p1_turn(board)
            if tic_tac_toe(board):
                p1_win += 1
                p3_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name1} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name1
                winner_player = player1
                loser_name = name3
                loser_player = player3
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            p3_turn(board)
            if tic_tac_toe(board):
                p3_win += 1
                p1_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name3} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
        else:
            p3_turn(board)
            if tic_tac_toe(board):
                p3_win += 1
                p1_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name3} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
                break
            p1_turn(board)
            if tic_tac_toe(board):
                p1_win += 1
                p3_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name1} is the winner!\n')
                print(f'Current Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name1
                winner_player = player1
                loser_name = name3
                loser_player = player3
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name1} {str(p1_win)} wins, {str(p1_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name1
                loser_player = player1
                game_over = True
    play_again()


def do_round_p2vsp3(board):
    global p2_win
    global p2_loss
    global p3_win
    global p3_loss
    global winner_name
    global winner_player
    global loser_name
    global loser_player
    global game_over
    while not game_over:
        if winner_name == name2:
            p2_turn(board)
            if tic_tac_toe(board):
                p2_win += 1
                p3_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name2} is the winner!\n')
                print(f'Current Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name3
                loser_player = player3
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
                break
            p3_turn(board)
            if tic_tac_toe(board):
                p3_win += 1
                p2_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name3} is the winner!\n')
                print(f'Current Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
        else:
            p3_turn(board)
            if tic_tac_toe(board):
                p3_win += 1
                p2_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name3} is the winner!\n')
                print(f'Current Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
                break
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
                break
            p2_turn(board)
            if tic_tac_toe(board):
                p2_win += 1
                p3_loss += 1
                draw_board(board)
                print(f'\nTic-Tac-Toe, Three-in-a-row!\n{name2} is the winner!\n')
                print(f'Current Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name2
                winner_player = player2
                loser_name = name3
                loser_player = player3
                game_over = True
            elif cats_game(board):
                draw_board(board)
                print('\nCat\'s Game. Wonk Wonk')
                print(f'\nCurrent Score:\n{name2} {str(p2_win)} wins, {str(p2_loss)} losses')
                print(f'{name3} {str(p3_win)} wins, {str(p3_loss)} losses\n')
                winner_name = name3
                winner_player = player3
                loser_name = name2
                loser_player = player2
                game_over = True
    play_again()


blah = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

name1 = ''
player1 = ''
name2 = ''
player2 = ''
name3 = ''
player3 = ''
winner_name = ''
winner_player = ''
loser_name = ''
loser_player = ''
p1_win = 0
p1_loss = 0
p2_win = 0
p2_loss = 0
p3_win = 0
p3_loss = 0
game_over = False
play = True
p1_continue = True
p2_continue = True

#### test board ####
#blah = [[1,'O','X'],
#         ['O','X','O'],
#         ['O','X','O']]

initialize()
while play:
    do_round_p1vsp2(blah)
while p1_continue:
    do_round_p1vsp3(blah)
while p2_continue:
    do_round_p2vsp3(blah)
print('\nGAME OVER\n\n'
      f'Final Score:\n{name1} - {str(p1_win)} wins, {str(p1_loss)} losses\n'
      f'{name2} - {str(p2_win)} wins, {str(p2_loss)} losses')
if name3 in (winner_name, loser_name):
    print(f'{name3} - {str(p3_win)} wins, {str(p3_loss)} losses\n')
else:
    print(f'\nGoodbye {winner_name} and {loser_name}.\nTHANKS FOR PLAYING!\nBrought to you by '
          f'Nintendo of Monterey Park')

