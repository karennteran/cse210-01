


def main():

    player_1 = input("DO YOU WANT 'O' OR 'X'? ")

    if player_1 == "o":
        print(grid_board())
        player_1 = int(input("where do you want to place your 'O'?"))
        print(grid_board_o(player_1))
    else:
        int(input("where do you want to place your 'x'? "))
        print(grid_board_x(player_1))







# drawing the grid
def grid_board():
    line_1 = print("1 | 2 | 3 ")
    divide_board = print("-+-+-+-+-+-")
    line_3 = print("4 | 5 | 6 ")
    divide_board = print("-+-+-+-+-+-")
    line_5 = print("7 | 8 | 9 ")
    

def grid_board_o(player_1):
    if player_1 == 1:
        line_1 = print("O | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 2:
        line_1 = print("1 | O | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 3:
        line_1 = print("1 | 2 | O")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 4:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("O | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 5:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | O | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 6:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | O ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 7:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("O | 8 | 9")
    elif player_1 == 8:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | O | 9")
    elif player_1 == 9:
        line_1 = print("1 | 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | O")


def grid_board_x(player_1):
    if player_1 == 1:
        line_1 = print("X| 2 | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")
    elif player_1 == 2:
        line_1 = print("1 | X | 3")
        divide_board = print("-+-+-+-+-+-")
        line_3 = print("4 | 5 | 6 ")
        divide_board = print("-+-+-+-+-+-")
        line_5 = print("7 | 8 | 9")




# # Call main to start this program.
if __name__ == "__main__":
    main()