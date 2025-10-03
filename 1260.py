from collections import deque, defaultdict

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order
node_num, edge_num, start = map(int, input().split())
graph = defaultdict(list)


for i in range(edge_num):
    node1, node2 = map(int, input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

bfs_order = bfs(graph, start)
dfs(graph, start)
print()
for i in bfs_order:
    print(i, end=' ')