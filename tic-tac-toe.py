    
import random

def isWin(board,symbol,x,y):
    colWin, rowWin, dia1Win, dia2Win = True, True, True, True
    for i in range(len(board)):
        if board[x][i] != symbol:
            rowWin = False
        if board[i][y] != symbol:
            colWin = False
    for i in range(len(board)):
        for j in range(len(board)):
            if i+j == 2 and board[i][j] != symbol:
                dia1Win = False
            if i-j == 0 and board[i][j] != symbol:
                dia2Win = False
    if any([colWin, rowWin, dia1Win, dia2Win]):
        return True
    else:
        return False

def opponentWin(board,symbol):
    colWin, rowWin, dia1Win, dia2Win = 0,0,0,0
    emptyRow, emptyCol, emptydia1, emptydia2 = 0,0,0,0
    rowPos , colPos, dia1Pos, dia2Pos = [],[],[],[]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == symbol:
                rowWin+=1
            elif board[i][j] == "":
                emptyRow+=1
                rowPos.append(i)
                rowPos.append(j)
        if rowWin == 2 and emptyRow == 1:
            return [True, rowPos]
        rowWin = 0
        emptyRow = 0
        rowPos = []

    for j in range(len(board)):
        for i in range(len(board)):
            if board[i][j] == symbol:
                colWin+=1
            elif board[i][j] == "":
                emptyCol+=1
                colPos.append(i)
                colPos.append(j)
        if colWin == 2 and emptyCol == 1:
            return [True, colPos]
        colWin = 0
        emptyCol = 0
        colPos = []

    
    for i in range(len(board)):
        for j in range(len(board)):
            if i+j == 2 and board[i][j] == symbol:
                dia1Win += 1
            elif i+j == 2 and board[i][j] == "":
                emptydia1 += 1
                dia1Pos.append(i)
                dia1Pos.append(j)
            elif i-j == 0 and board[i][j] == symbol:
                dia2Win += 1
            elif i-j == 0 and board[i][j] == "":
                emptydia2 += 1
                dia2Pos.append(i)
                dia2Pos.append(j)
    if dia1Win == 2 and emptydia1 == 1:
        return [True, dia1Pos]
    elif dia2Win == 2 and emptyCol == 1:
        return [True, dia2Pos]
    else:
        return [False,[]]
    

def getPosition(board,computerSymbol,playerSymbol):
    if isEmpty(board):
        return random.choice([[0,0],[0,2],[2,0],[2,2]])
    corners = [[0,0],[0,2],[2,0],[2,2]]
    count = 0
    single = 0
    pos = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                count+=1
            elif board[i][j] == playerSymbol:
                single += 1
                pos.append([i,j])
    if count == 8 and single == 1 and pos[0] in corners:
        return [1,1]
    possiblePositions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "" and [i,j] not in possiblePositions:
                possiblePositions.append([i,j])
                board[i][j] = computerSymbol
                if isWin(board,computerSymbol,i,j):
                    return [i,j]
                else:
                    board[i][j] = ""
    playerWin = opponentWin(board,playerSymbol)
    if playerWin[0]:
        return playerWin[1]
    else:
        return random.choice(possiblePositions)
    
def isBoardFull(board):
    flag  = 0
    for i in board:
        for j in i:
            if j == '':
                return False
    return True

def isEmpty(board):
    for i in board:
        for j in board:
            if j != '':
                return False
    return True

def printBoard(board):
    for i in range(len(board)):
        print("|",end=" ")
        for j in range(len(board)):
            print(board[i][j],"|",end=" ")
        print('\n')
    
board = [[""] * 3 for i in range(3)]
printBoard(board)
playerSymbol = input("Enter sysmbol you want X or O:").upper()
while playerSymbol.upper() not in ["X","O"]:
    print("Enter correct symbol......")
    playerSymbol = input("Enter sysmbol you want X or O:")
if playerSymbol.upper() == "X":
    computerSymbol = "O"
elif playerSymbol.upper() == "O":
    computerSymbol = "X"
turn = playerSymbol
positions = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
print("Your symbol : ",playerSymbol)
print("My symbol : ",computerSymbol)
turn = random.choice([computerSymbol,playerSymbol])
while True:
    if turn == playerSymbol:
        print("It's your turn")
        position = 0
        position = int(input("Enter desired position(1-9):"))
        [x,y] = positions[position-1]
        while board[x][y] != "":
            print("already filled.......")
            position = int(input("Enter desired position(1-9):"))
            [x,y] = positions[position-1]
        board[x][y] = playerSymbol
        printBoard(board)
        if isWin(board,playerSymbol,x,y):
            print("You won.... :)")
            break
        turn = computerSymbol
        if isBoardFull(board):
            print(".........Tie.........")
            break
    else:
        print("It's my turn")
        
            
        boardDup = board
        [x,y] = getPosition(boardDup,computerSymbol,playerSymbol)
        board[x][y] = computerSymbol
        printBoard(board)
        if isWin(board,computerSymbol,x,y):
            print("You lose..... :(")
            break
        turn = playerSymbol
        if isBoardFull(board):
            print(".........Tie.........")
            break
import msvcrt as m
def wait():
    m.getch()
