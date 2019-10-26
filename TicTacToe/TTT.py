import random
"""
x = random.randint(0,9)
"""
# Draw board
board = ["-", "-", "-", 
         "-", "-", "-",
         '-', "-", "-"]

# Turn Count
TurnCount = 0

gameLive = True
# Draws Game Board
def drawBoard():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")

def userInput():
    validInput = False
    while not validInput:
        where = input("\nSelect Postion between 1 - 9:\n")
        # Makes where the player can not pick a postion that is already occupied
        if board[int(where)-1] == "-" and int(where) >= 0 and int(where) <= 9:
            board[int(where)-1] = 'X'
            validInput = True
        else:
            print("Please Select another Place\n")
            
def compInput():
    goodNum = False

    while not goodNum:
        compNum = random.randint(0,8)
        if board[compNum] == "-":
            board[compNum] = "O"
            goodNum = True
            break

def winCheck():
    if TurnCount >= 3:
        if rowCheckO or rowCheckX:
            return False
        return True
    return True

def rowCheckX():
    # Row Check X
    if board[0] == 'X'and board[1] == "X" and board[2] == "X": 
        win() 
        return True
    if board[3] == 'X'and board[4] == "X" and board[5] == "X": 
        win() 
        return True
    if board[6] == 'X'and board[7] == "X" and board[8] == "X": 
        win() 
        return True
    return False

def rowCheckO():
    # Row Check O
    if board[0] == 'O'and board[1] == "O" and board[2] == "O": 
        lose() 
        return True
    if board[3] == 'O'and board[4] == "O" and board[5] == "O": 
        lose() 
        return True
    if board[6] == 'O'and board[7] == "O" and board[8] == "O": 
        lose() 
        return True
    return False
def win():
    print("\nCongrats! You Beat The Game\n")

def lose():
    print("\nDarn! You Lost The Game!\n")

while gameLive:
    # Draw Board
    drawBoard()

    # User Input Human Player always X
    userInput()
    
    # Display and increment by 1
    TurnCount += 1
    print("\nTurn Count:")
    print(TurnCount)
    print("\n")

    drawBoard()

    if winCheck == False:
        break
    
    # Computer input
    compInput()
    drawBoard()
    gameLive = winCheck()
    # Check Win
        # Check Rows
        # Check Columns
        # Check Diaganles
        # Check Draw
        # Who?

    # Flip Players

