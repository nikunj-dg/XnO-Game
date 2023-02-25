#-----------------FNS-----------------#

def display_board(board):
    for row in board:
        print(''.join(row))

def update_board(board, in_list, pos):
    if pos != ' ':
        if pos == 7 or pos == 8 or pos == 9:
            i = 1
            if pos == 7:
                k = 1
            if pos == 8:
                k = 5
            if pos == 9:
                k = 9

        if pos == 4 or pos == 5 or pos == 6:
            i = 5
            if pos == 4:
                k = 1
            if pos == 5:
                k = 5
            if pos == 6:
                k = 9

        if pos == 1 or pos == 2 or pos == 3:
            i = 9
            if pos == 1:
                k = 1
            if pos == 2:
                k = 5
            if pos == 3:
                k = 9

        board[ i ][ k ] = in_list[pos]

    return board

def input_pos(player, inp_list):
    pos = 'WRONG'
    options = ['1', '2', '3', '4', '5','6', '7', '8', '9']

    while True:
        pos = input(player + " Position : ")
        if ( pos in options ) and ( inp_list[int(pos)] is ' ' ):
            break
        print("Invalid input")

    return int(pos)

def check_board(board, char):
    if board[1][1]  == char and board[1][5] == char and board[1][9] == char:
        return board[1][1]
    if board[5][1]  == char and board[5][5]  == char and board[9][9] == char:
        return board[5][1]
    if board[9][1]  == char and board[9][5]  == char and board[9][9] == char:
        return board[9][1]
    if board[1][1]  == char and board[5][1]  == char and board[9][1] == char:
        return board[1][1]
    if board[1][5]  == char and board[5][5]  == char and board[9][5] == char:
        return board[1][5]
    if board[1][9]  == char and board[5][9]  == char and board[9][9] == char:
        return board[1][9]
    if board[1][1]  == char and board[5][5]  == char and board[9][9] == char:
        return board[1][1]
    if board[9][1]  == char and board[5][5]  == char and board[1][9] == char:
       return board[9][1]

    return 'False'


#--------------------MAIN----------------------#

replay = 'Yes'
while replay == 'Yes':
    #board:    #1    2    3    4    5    6    7    8    9   10   11
    board = [ [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #1 - empty
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #2 - data
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #3 - empty
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], #4 - dividing
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #5 - empty
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #6 - data
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #7 - empty
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], #8 - dividing
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #9 - empty
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '], #10 - data
              [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '] ] #11 - empty

    input_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    p1 = 'WRONG'
    options = ['X', 'O']

    while p1 not in options:
        p1 = input("Player 1 is 'X' or 'O' : ")
        if p1 not in options:
            print("Invalid input")

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    print("Player 2 is", p2)

    #------GAME LOGIC-------#
    
    win = 'False'
    while win == 'False':
        position = input_pos('P1', input_list)
        input_list[position] = p1
        board = update_board(board, input_list, position)
        display_board(board)
        win = check_board(board, p1)
        if ' ' not in input_list:
            print("It's a DRAW!")
            win = ' '
            replay = input("Do you want to play again, 'Y' or 'N' : ")
            break

        if win != 'False':
            print("Player 1 has won!!!!!")
            replay = input("Do you want to play again, 'Y' or 'N' : ")
            break

        position = input_pos('P2', input_list)
        input_list[position] = p2
        board = update_board(board, input_list, position)
        display_board(board)
        win = check_board(board, p2)
        if win != 'False':
            print("Player 1 has won!!!!!")
            replay = input("Do you want to play again, 'Yes' or 'No' : ")
            break
