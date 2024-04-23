# recursive
def dfs(graph, starting_node):
    res = []
    visited = {0}

    def traverse(node):
        if node not in visited:
            visited.add(node)
            res.append(node)
            
            for child in graph[node]:
                traverse(child)

    traverse(starting_node)

    return res

# iterative
def dfs_iterative(graph, starting_node):
    res = []
    stack = [starting_node]
    visited = []

    while stack:
        node = stack.pop()

        if node and node not in visited:
            visited.append(node)
            res.append(node)

        for child in reversed(graph[node]):
            if child not in visited:
                stack.append(child)
    
    return res

adj = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3, 8],
    5: [5],
    6: [2],
    7: [3, 8],
    8: [4, 7],
}

print(dfs(adj, 1))
print(dfs_iterative(adj, 1))