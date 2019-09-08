import random
#print how the board looks
def thisBoardLooksLike():
     print('   |   |')
     print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
     print('   |   |')

def displayBoard(board):
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
 
#choose the input you want to give
def playerInput():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    print('Current Board state :')
    displayBoard(theBoard)
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# randomely choose who plays first
def checkFirstPlayer():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

#check if the player wants to play again
def playAgain():
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')

#store the move
def makeMove(board, letter, move):
    board[move] = letter

# condition where the winner is chosen
def isWinner(b, l):
    return ((b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[4] == l and b[1] == l) or
            (b[8] == l and b[5] == l and b[2] == l) or
            (b[9] == l and b[6] == l and b[3] == l) or
            (b[7] == l and b[5] == l and b[3] == l) or
            (b[9] == l and b[5] == l and b[1] == l))

def isSpaceFree(board, move):
    return board[move]

def getPlayerMove(board):
     '''
     get the player move, check if it is between 1-9. If not ask to choose a different cell
     '''
    move = ' '
    while True:
        print('What is your move? (1-9)')
        move = input()
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('move should be between 1-9')
        elif board[int(move)] != ' ':
            print('Choose a different cell')
        else:
            break
    return int(move)

#choose random move from list
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

 #Get the computer move
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'

    else:
        playerLetter = 'X'
    chooseList = [1,3,7,9] # choose the corners first
    while len(chooseList) > 0:
        move = chooseRandomMoveFromList(board, chooseList)
        if board[move] == ' ':
            return move
        chooseList.remove(move)

    #if not corners go for the center position
    if board[5] == ' ':
        return 5

     #choose the remaining if nothing else is available
    chooseList = [2,4,6,8]
    while len(chooseList) > 0:
        move = chooseRandomMoveFromList(board, chooseList)
        if board[move] == ' ':
            return move
        chooseList.remove(move)
    return -1

#check if the board is full for tie condition
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print('Welcome to Tic Tac Toe!')
print('This is how the board looks like, choose positions based on this board')
thisBoardLooksLike()

while True:
    theBoard = [' ']*10
    playerLetter, computerLetter = playerInput()
    turn = checkFirstPlayer()
    print('The '+ turn + ' will go first.')
    gameIsOn = True

    while gameIsOn:
        if turn == 'player':
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            print('Current Board state :')
            displayBoard(theBoard)
            if isWinner(theBoard, playerLetter):
                print('Yaay! You have won the game!')
                gameIsOn = False
            else:
                if isBoardFull(theBoard):
                    print('The game is a Tie!')
                    gameIsOn = False
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            print('Current Board state :')
            displayBoard(theBoard)
            if isWinner(theBoard, computerLetter):
                print('You lose to the Computer!')
                gameIsOn = False
            else:
                if isBoardFull(theBoard):
                    print('It is a tie!')
                    gameIsOn = False
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
            







            

            
    
