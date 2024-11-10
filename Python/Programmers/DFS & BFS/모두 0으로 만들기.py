import sys 

sys.setrecursionlimit(10**6)
answer = 0

def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = [[] for _ in range(len(a))]
    for node_a, node_b in edges:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
        
    def dfs(child, parent, graph, a):
        global answer
        for c in graph[child]:
            if c != parent:
                dfs(c, child, graph, a)
        a[parent] += a[child]
        answer += abs(a[child])
        
    dfs(0, 0, graph, a)
    return answer