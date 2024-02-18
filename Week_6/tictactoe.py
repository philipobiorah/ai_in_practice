import sys
move = -1
n = 0
nodes = 0
def evaluateBoard(board):
    global n
    #Checking for rows
    cnt = 0
    for i in range(n):
        res = 0
        for j in range(n):
           res += board[cnt * n + j] 
        cnt += 1
        if res == n:
            return 1
        elif res == -n:
            return -1
        
    #Checking for columns
    for i in range(n):
        res = 0
        for j in range(n):
            res += board[i + n * j]
        if res == n:
            return 1
        elif res == -n:
            return -1
            
    #Checking for diagonals
    res = res2 = 0
    for i in range(n):
        res += board[i * (n + 1)]   
        res2 += board[(i + 1) * (n - 1)]
    if n in [res, res2]:
        return 1
    elif -n in [res, res2]:
        return -1

    return 0
    
def checkNonTerminal(board):
   for pos in board:
       if pos == 0:
           return 1
   return 0

def getScore(board, depth):
    if evaluateBoard(board) == 1:
        return 10 - depth
    elif evaluateBoard(board) == -1:
        return depth - 10
    else:
        return 0

def minimax(board, turn, depth):
    global nodes
    if evaluateBoard(board) == 0 and checkNonTerminal(board) == 0:
        return getScore(board, depth)
    global move
    moves = list()
    scores = list()
    nodes += 1
    for square, pos in enumerate(board):
        if pos == 0:
            new_board = board.copy()
            new_board[square] = turn
            moves.append(square)
            
            if evaluateBoard(new_board) in [1, -1] or checkNonTerminal(new_board) == 0:
                move = square
                return getScore(new_board, depth)
            scores.append(minimax(new_board, turn * -1, depth + 1))
    
    if turn == 1:
        move = moves[scores.index(max(scores))]
        return max(scores)
    elif turn == -1:
        move = moves[scores.index(min(scores))]
        return min(scores)
    
def displayBoard(board):
    global n
    for i in range(n):
        for j in range(n):
            if board[n*i+j] == 1:
                print("x",end=" ")
            elif board[n*i+j] == -1:
                print("o", end=" ")
            else:
                print(".", end = " ")
        print()
    print()
    
def main():      
    global n 
    global move
    n = 3
    first_turn = input("Would you like to go first (Y/N)?: ")
    if first_turn in ['Y', 'y']:
        first_turn = -1
        cnt = 1
    else:
        first_turn = 1
        cnt = 2
    board = [0] * 9
    displayBoard(board)
    while evaluateBoard(board) == 0 and checkNonTerminal(board) == 1:
        
        if cnt % 2 == 0:
            minimax(board, 1, 0)
            #print(score)
            board[move] = 1
            displayBoard(board)
        else:
            choice = eval(input("Enter your choice (1-9): "))
            if board[choice - 1] != 0:
                print("No cheating!")
                sys.exit([0])
            else:
                board[choice - 1] = -1
                displayBoard(board)
        cnt += 1
    
    if evaluateBoard(board) == 1:
        print("You lose!")
    elif evaluateBoard(board) == -1:
        print("You win!")
    else:
        print("It's a draw!")
    
    print(nodes,"nodes")

main()
