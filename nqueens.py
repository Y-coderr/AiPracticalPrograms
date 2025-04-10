def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def dfs(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                dfs(row + 1, board, solutions)

    solutions = []
    dfs(0, [-1]*n, solutions)
    return solutions

# Print solutions in board format
def print_solutions(solutions):
    for sol in solutions:
        for i in sol:
            row = ['.']*len(sol)
            row[i] = 'Q'
            print("".join(row))
        print()

# Example: Solve 4-Queens
n = 4
results = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(results)}")
print_solutions(results)
