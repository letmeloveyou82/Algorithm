import sys
from collections import deque

def is_bipartite_graph(start):
    q = deque([start])
    color[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if color[i] == 0:
                color[i] = -color[v]
                q.append(i)
            elif color[i] == color[v]:
                return False
    return True

input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipartite = True
    for v in range(1, V+1):
        if color[v] == 0:
            if not is_bipartite_graph(v):
                bipartite = False
                break
    print("YES" if bipartite else "NO")