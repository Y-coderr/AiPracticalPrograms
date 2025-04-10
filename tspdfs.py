import sys

def tsp_dfs(graph, start):
    n = len(graph)
    visited = [False] * n
    min_path = {
        "cost": sys.maxsize,
        "path": []
    }

    def dfs(curr, count, cost, path):
        if count == n and graph[curr][start] > 0:
            total_cost = cost + graph[curr][start]
            if total_cost < min_path["cost"]:
                min_path["cost"] = total_cost
                min_path["path"] = path + [start]
            return

        for i in range(n):
            if not visited[i] and graph[curr][i] > 0:
                visited[i] = True
                dfs(i, count + 1, cost + graph[curr][i], path + [i])
                visited[i] = False

    visited[start] = True
    dfs(start, 1, 0, [start])
    return min_path

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_node = 0
result = tsp_dfs(graph, start_node)

print("Minimum cost:", result["cost"])
print("Path taken: ", " -> ".join(map(str, result["path"])))
