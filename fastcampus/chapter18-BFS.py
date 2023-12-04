# 너비 우선 탐색 (Breadth-First Search)
def bfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)    # 특정 index(여기선 0)를 뽑음
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))
