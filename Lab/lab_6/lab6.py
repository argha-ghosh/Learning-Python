# Hill Climbing Search for 8-Puzzle
# Heuristic: Number of misplaced tiles

import copy

# Goal state
goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# Initial state
current_state = [
    [1, 2, 3],
    [8, 6, 0],
    [7, 5, 4]
]

# Heuristic function
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Hill Climbing Algorithm
def hill_climbing(start):
    current = start
    current_h = heuristic(current)

    while True:
        neighbors = get_neighbors(current)
        next_state = current
        next_h = current_h

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < next_h:
                next_state = neighbor
                next_h = h

        if next_h >= current_h:
            break

        current = next_state
        current_h = next_h
        print_state(current, current_h)

    return current

# Print state
def print_state(state, h):
    print("Heuristic =", h)
    for row in state:
        print(row)
    print()

# Run
print("Initial State:")
print_state(current_state, heuristic(current_state))

result = hill_climbing(current_state)

print("Final State:")
print_state(result, heuristic(result))

if heuristic(result) == 0:
    print("Goal state reached!")
else:
    print("Stuck in local optimum.")
