import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if not moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best = min(best, score)
        return best


def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O")

    while True:
        print_board(board)
        if check_winner(board):
            print(f"Winner is {check_winner(board)}!")
            break
        if not moves_left(board):
            print("It's a draw!")
            break

  
        x, y = map(int, input("Enter row and col (0-2): ").split())
        if board[x][y] != ' ':
            print("Invalid move, try again.")
            continue
        board[x][y] = 'X'

        if check_winner(board) or not moves_left(board):
            print_board(board)
            if check_winner(board):
                print("You win!")
            else:
                print("It's a draw!")
            break


        i, j = best_move(board)
        board[i][j] = 'O'

        if check_winner(board):
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    play_game()
