import random

grid = [
    ['.', '.', '.', '.', 'G'],
    ['.', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.'],
    ['A', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.']
]

agent_pos = [3, 0]

def print_grid():
    for row in grid:
        print(" ".join(row))
    print()

def valid_moves(x, y):
    moves = []
    directions = {'UP': (-1,0), 'DOWN': (1,0), 'LEFT': (0,-1), 'RIGHT': (0,1)}
    for d, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != '#':  # avoid obstacles
                moves.append((d, (nx, ny)))
    return moves

def reflex_agent(x, y):
    moves = valid_moves(x, y)
    if not moves:
        return (x, y)
    
    gx, gy = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'G':
                gx, gy = i, j


    best_move = min(moves, key=lambda m: abs(m[1][0]-gx) + abs(m[1][1]-gy))
    return best_move[1]

print("Initial Grid:")
print_grid()

while True:
    x, y = agent_pos
    if grid[x][y] == 'G':
        print("Agent reached the goal!")
        break
    
    nx, ny = reflex_agent(x, y)
    
    grid[x][y] = '.'
    agent_pos = [nx, ny]
    if grid[nx][ny] != 'G':
        grid[nx][ny] = 'A'

    print_grid()
