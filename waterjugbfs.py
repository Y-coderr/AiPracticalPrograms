from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == target or b == target:
            return f"Found solution: Jug1 = {a}, Jug2 = {b}"

        # All possible operations
        queue.extend([
            (jug1, b),      # Fill Jug1
            (a, jug2),      # Fill Jug2
            (0, b),         # Empty Jug1
            (a, 0),         # Empty Jug2
            (min(a + b, jug1), max(0, b - (jug1 - a))),  # Pour Jug2 -> Jug1
            (max(0, a - (jug2 - b)), min(a + b, jug2))   # Pour Jug1 -> Jug2
        ])
    return "No solution"

#  Take input from user
jug1 = int(input("Enter Jug1 capacity: "))
jug2 = int(input("Enter Jug2 capacity: "))
target = int(input("Enter target amount: "))

print(water_jug_bfs(jug1, jug2, target))
