import sys
board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
player='X'
bot='O'

def displayBoard():
    print(board[1],'|',board[2],'|',board[3])
    print(board[4],'|',board[5],'|',board[6])
    print(board[7],'|',board[8],'|',board[9])

def insert(letter,position):
    if spaceEmpty(position):
        board[position]=letter
        displayBoard()
        if checkDraw():
            print("Draw!")
        elif checkWin():
            print(letter," won!")
            sys.exit()
    else:
        print("Space occupied! Try again")
        position=int(input("Enter position: "))
        insert(letter,position)
    
def checkWin():
    if (board[1]==board[2] and board[1]==board[3] and board[1]!=' '):
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4]!=' '):
        return True
    elif (board[7]==board[8] and board[7]==board[9] and board[7]!=' '):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1]!=' '):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3]!=' '):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1]!=' '):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2]!=' '):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3]!=' '):
        return True
    else:
        return False

def checkDraw():
    for i in board.keys():
        if board[i]==' ':
            return False
    return True

def spaceEmpty(position):
    if board[position]==' ':
        return True
    return False

def playerMove():
    position=int(input("Player X: "))
    insert('X',position)

def compMove():
    position=int(input("Player O: "))
    insert('O',position)

displayBoard()
while not checkWin():
    compMove()
    playerMove()