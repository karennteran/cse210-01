

position = [0,1,2,3,4,5,6,7,8,9]
print('\n\nTic Tac Toe\n\n')

print('player 1 (1) - player 2 (2) ')
print()

print('     |     |       ')
print(' ',position[1] ,' | ' ,position[2] ,' | ' , position[3] )

print('_____|_____|_____')
print('     |     |     ')

print(' ',position[4] ,' | ' ,position[5] ,' | ' , position[6] )

print('_____|_____|_____')
print('     |     |     ')

print(' ',position[7] ,' | ' ,position[8] ,' | ' , position[9] )

print('     |     |       ')
position1 = (' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')


def main():

    player = 1
    status = -1

    while status == -1:
        board()

        if player%2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input('Enter a number'))

        if player == 1:
            mark = '1'
        else:
            mark = '2'

        if choice == 1 and position[1] == 1:
            position1[1] = mark
        elif choice == 2 and position[2] == 2:
            position1[2] = mark
        elif choice == 3 and position[3] == 3:
            position1[3] = mark
        elif choice == 4 and position[4] == 4:
            position1[4] = mark
        elif choice == 5 and position[5] == 5:
            position1[5] = mark
        elif choice == 6 and position[6] == 6:
            position1[6] = mark
        elif choice == 7 and position[7] == 7:
            position1[7] = mark
        elif choice == 8 and position[8] == 8:
            position1[8] = mark
        elif choice == 9 and position[9] == 9:
            position1[9] = mark
        else:
            print('Invalid move')
            player -= 1

        status = game_status()
        player += 1
    if(status == 1 or status == 0):
        board()
    print('RESULT')
    if status == 1:
        print('player', player-1, 'WIN')
    else:
        print('Game Draw')

################################################################
# funtion to return game status
# 1 for game is over with result
# -1 for game is in progress
# 0 game is over and no results.
# #################################################################

def game_status():
    if position1[1] == position1[2] and position1[2] == position1[3] and position1[1]!=' ' and position1[2]!=' ' and position1[3]!=' ':
        return 1
    elif position1[4] == position1[5] and position1[5] == position1[6] and position1[4]!=' ' and position1[5]!=' ' and position1[6]!=' ':
        return 1
    elif position1[7] == position1[8] and position1[8] == position1[9] and position1[7]!=' ' and position1[8]!=' ' and position1[9]!=' ':
        return 1
    elif position1[1] == position1[4] and position1[4] == position1[7] and position1[1]!=' ' and position1[4]!=' ' and position1[7]!=' ':
        return 1
    elif position1[2] == position1[5] and position1[5] == position1[8] and position1[2]!=' ' and position1[5]!=' ' and position1[8]!=' ':
        return 1
    elif position1[3] == position1[6] and position1[6] == position1[9] and position1[3]!=' ' and position1[6]!=' ' and position1[9]!=' ':
        return 1
    elif position1[1] == position1[5] and position1[5] == position1[9] and position1[1]!=' ' and position1[5]!=' ' and position1[9]!=' ':
        return 1
    elif position1[3] == position1[5] and position1[5] == position1[7] and position1[3]!=' ' and position1[5]!=' ' and position1[7]!=' ':
        return 1
    elif position1[1] != 1 and position1[2] != 2 and position1[3] != 3 and position1[4] != 4 and position1[5] != 5 and position1[6] != 6 and position1[7] != 7 and position1[8] != 8 and position1[9] != 9:
        return 0
    else:
        return -1


# ##################################################################
#  function to draw the board
#  of tic tac Toe
# ##################################################################

def board():

    print('player 1 (1) - player 2 (2) ')
    print()

    print('     |     |      ')
    print(' ',position1[1] ,' | ' ,position1[2] ,' | ' , position1[3] )

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ',position1[4] ,' | ' ,position1[5] ,' | ' , position1[6] )

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ',position1[7] ,' | ' ,position1[8] ,' | ' , position1[9] )

    print('     |     |      ')


main()


# ######################################################
# practice code:
# drawing the grid
# def grid_board():
#     line_1 = print("1 | 2 | 3 ")
#     divide_board = print("-+-+-+-+-+-")
#     line_3 = print("4 | 5 | 6 ")
#     divide_board = print("-+-+-+-+-+-")
#     line_5 = print("7 | 8 | 9 ")
    

# def grid_board_o(player_1):
#     if player_1 == 1:
#         line_1 = print("O | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 2:
#         line_1 = print("1 | O | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 3:
#         line_1 = print("1 | 2 | O")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 4:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("O | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 5:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | O | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 6:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | O ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 7:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("O | 8 | 9")
#     elif player_1 == 8:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | O | 9")
#     elif player_1 == 9:
#         line_1 = print("1 | 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | O")


# def grid_board_x(player_1):
#     if player_1 == 1:
#         line_1 = print("X| 2 | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")
#     elif player_1 == 2:
#         line_1 = print("1 | X | 3")
#         divide_board = print("-+-+-+-+-+-")
#         line_3 = print("4 | 5 | 6 ")
#         divide_board = print("-+-+-+-+-+-")
#         line_5 = print("7 | 8 | 9")




# # # Call main to start this program.
# if __name__ == "__main__":
#     main()