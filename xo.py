from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[0][0]+'       '+board[0][1]+'   |   '+board[0][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[1][0]+'       '+board[1][1]+'   |   '+board[1][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[2][0]+'       '+board[2][1]+'   |   '+board[2][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        r=int(input('Enter your move: '))
        board[(r-1)//3][r%3-1]='O'
    except:
        print('Wrong input')
        display_board(board)
        enter_move(board)
    return board
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    i=0
    lst=()
    for x in board:
        for y in x:
         i+=1
         if y!='O' and y!='X':
            lst+=((i-1)//3, (i-1)%3),
        
    return lst
    
    

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    if (board[0][0]==sign)and(board[1][0]==sign)and(board[2][0]==sign):
        return True
    elif (board[0][1]==sign)and(board[1][1]==sign)and(board[2][1]==sign):
        return True   
    elif (board[0][2]==sign)and(board[1][2]==sign)and(board[2][2]==sign):
        return True   
    elif (board[0][0]==sign)and(board[0][1]==sign)and(board[0][2]==sign):
        return True
    elif (board[1][0]==sign)and(board[1][1]==sign)and(board[1][2]==sign):
        return True   
    elif (board[2][0]==sign)and(board[2][1]==sign)and(board[2][2]==sign):
        return True
    elif (board[0][0]==sign)and(board[1][1]==sign)and(board[2][2]==sign):
        return True   
    elif (board[2][0]==sign)and(board[1][1]==sign)and(board[0][2]==sign):
        return True
    else: 
        return False

#def draw_move(board):
    # The function draws the computer's move and updates the board.

board=[[str(x) for x in range((y-1)*3+1,(y-1)*3+4)] for y in range(1,4)]
s=0
fin=True
while fin:
    if not s:
       board[1][1]='X' 
    s+=1
    display_board(board)
    enter_move(board)
    lst=make_list_of_free_fields(board)
    rlst=lst[randrange(len(lst))]
    board[rlst[0]][rlst[1]]='X'
    if victory_for(board, 'O'):
        print('You won')
        fin=False
    elif victory_for(board, 'X'):
        print('Computer wins')
        fin=False
    