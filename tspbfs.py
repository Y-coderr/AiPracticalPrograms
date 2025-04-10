from collections import deque
from itertools import permutations

# Example cost matrix
graph = [
    [0, 10, 15, 20],   # distances from city 0
    [10, 0, 35, 25],   # distances from city 1
    [15, 35, 0, 30],   # distances from city 2
    [20, 25, 30, 0]    # distances from city 3
]

def tsp_bfs(graph):
    n = len(graph)
    min_cost = float('inf')
    best_path = []

    cities = list(range(1, n))
    for perm in permutations(cities):
        cost = 0
        path = [0] + list(perm) + [0]  # start and end at 0
        for i in range(n):
            cost += graph[path[i]][path[i+1]]
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return min_cost, best_path

# Run TSP
cost, path = tsp_bfs(graph)
print(f"Minimum cost: {cost}")
print(f"Path: {' -> '.join(map(str, path))}")
