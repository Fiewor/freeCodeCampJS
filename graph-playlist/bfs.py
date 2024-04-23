# time complexity -> O(N) + O(2E)
# space complexity -> O(N)
from collections import deque

def bfs(graph, starting_node):
    queue = deque([starting_node])
    visited = {starting_node}
    res = []

    while(queue):
        node = queue.popleft()
        res.append(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return res

adj = {
    1: [2, 6],
    2: [1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4, 7],
    6: [1, 7, 8],
    7: [5, 6],
    8: [6],
}
print(bfs(adj, 1))