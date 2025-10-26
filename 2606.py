from collections import defaultdict

def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()

    visited.add(node)
    virus.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return virus

node_num = int(input())
edge_num = int(input())
graph = defaultdict(list)
virus = []

for i in range(edge_num):
    node1, node2 = map(int, input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

print(len(dfs(graph, 1))-1)