import sys

# Initialize global variables
move = -1  # Stores the AI's move
n = 0      # Size of the Tic Tac Toe board (n x n)
nodes = 0  # Counter for the number of nodes explored during the minimax search

# Function to evaluate the current state of the board
def evaluateBoard(board):
    global n
    # Checking for rows
    for i in range(n):
        res = 0
        for j in range(n):
            res += board[i * n + j] 
        if res == n:   # Player wins
            return 1
        elif res == -n:  # AI wins
            return -1
        
    # Checking for columns
    for i in range(n):
        res = 0
        for j in range(n):
            res += board[i + n * j]
        if res == n:
            return 1
        elif res == -n:
            return -1
            
    # Checking for diagonals
    res = res2 = 0
    for i in range(n):
        res += board[i * (n + 1)]   
        res2 += board[(i + 1) * (n - 1)]
    if n in [res, res2]:
        return 1
    elif -n in [res, res2]:
        return -1

    return 0
    
# Function to check if the game is still ongoing
def checkNonTerminal(board):
   for pos in board:
       if pos == 0:
           return 1
   return 0

# Function to assign a score to a board configuration
def getScore(board, depth):
    if evaluateBoard(board) == 1:
        return 10 - depth
    elif evaluateBoard(board) == -1:
        return depth - 10
    else:
        return 0

# Minimax algorithm for AI decision making
def minimax(board, turn, depth):
    global nodes
    # If game over or terminal state reached, return score
    if evaluateBoard(board) == 0 and checkNonTerminal(board) == 0:
        return getScore(board, depth)
    global move
    moves = list()
    scores = list()
    nodes += 1
    # Iterate through possible moves
    for square, pos in enumerate(board):
        if pos == 0:  # Check if the position is empty
            new_board = board.copy()
            new_board[square] = turn
            moves.append(square)
            # If current move leads to a win or loss, return score
            if evaluateBoard(new_board) in [1, -1] or checkNonTerminal(new_board) == 0:
                move = square
                return getScore(new_board, depth)
            # Recursively call minimax for opponent's turn
            scores.append(minimax(new_board, turn * -1, depth + 1))
    # Choose the best move based on maximizing or minimizing score
    if turn == 1:
        move = moves[scores.index(max(scores))]
        return max(scores)
    elif turn == -1:
        move = moves[scores.index(min(scores))]
        return min(scores)
    
# Function to display the Tic Tac Toe board
def displayBoard(board):
    global n
    for i in range(n):
        for j in range(n):
            if board[n * i + j] == 1:
                print("x", end=" ")  # Player's symbol
            elif board[n * i + j] == -1:
                print("o", end=" ")  # AI's symbol
            else:
                print(".", end=" ")  # Empty space
        print()
    print()

# Function to apply the player's move and display the board
def applyMoveAndDisplay(board, player, move):
    board[move] = player
    displayBoard(board)
    score = getScore(board, 0)  # Calculate the heuristic score for the current board state
    print("Heuristic Score:", score)

# Main function to start the game
def main():      
    global n 
    global move
    n = 3  # Size of the board (3x3)
    # Ask the player if they want to go first
    first_turn = input("Would you like to go first (Y/N)?: ")
    if first_turn in ['Y', 'y']:
        first_turn = -1  # Player goes first
        cnt = 1
    else:
        first_turn = 1   # AI goes first
        cnt = 2
    # Initialize the board
    board = [0] * 9
    displayBoard(board)  # Display the initial board
    # Game loop
    while evaluateBoard(board) == 0 and checkNonTerminal(board) == 1:
        if cnt % 2 == 0:  # AI's turn
            minimax(board, 1, 0)  # Calculate AI's move using minimax
            applyMoveAndDisplay(board, 1, move)  # Apply AI's move and display the board
        else:  # Player's turn
            choice = eval(input("Enter your choice (1-9): "))  # Ask player for their move
            if board[choice - 1] != 0:  # Check for cheating
                print("No cheating!")
                sys.exit([0])
            else:
                applyMoveAndDisplay(board, -1, choice - 1)  # Apply player's move and display the board
        cnt += 1  # Increment turn counter
    
    # Game over, determine the result
    if evaluateBoard(board) == 1:
        print("You lose!")
    elif evaluateBoard(board) == -1:
        print("You win!")
    else:
        print("It's a draw!")
    
    print(nodes, "nodes")  # Display the number of nodes explored during the game

# Start the game
main()