# Function to check if current state is goal
def is_goal(state, goal):
    return state == goal

# Function to move a block
def move_block(state, block, destination):
    new_state = [stack.copy() for stack in state]
    # Remove block from its current position
    for stack in new_state:
        if block in stack:
            stack.remove(block)
            break
    # Place block on destination
    if destination == "table":
        new_state.append([block])
    else:
        for stack in new_state:
            if stack and stack[-1] == destination:
                stack.append(block)
                break
    # Clean empty stacks
    new_state = [stack for stack in new_state if stack]
    return new_state

# Get possible moves
def get_moves(state):
    moves = []
    # You can move only top blocks
    top_blocks = [stack[-1] for stack in state]
    for block in top_blocks:
        for dest in top_blocks + ["table"]:
            if block != dest:
                moves.append((block, dest))
    return moves

# Breadth-First Search
def solve(initial, goal):
    queue = [(initial, [])]
    visited = []

    while queue:
        current, path = queue.pop(0)

        if current in visited:
            continue
        visited.append(current)

        if is_goal(current, goal):
            return path + [current]

        for block, dest in get_moves(current):
            new_state = move_block(current, block, dest)
            queue.append((new_state, path + [current]))

    return None

# Example usage
if __name__ == "__main__":
    initial_state = [['A', 'B'], ['C']]
    goal_state = [['C', 'B', 'A']]

    solution = solve(initial_state, goal_state)

    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")
