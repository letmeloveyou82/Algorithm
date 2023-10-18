import sys
sys.setrecursionlimit(100000) 
input = sys.stdin.readline

n, m = map(int, input().split()) # 노드 개수, 간선 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

# 덩어리 개수 구하기(연결된 노드들은 모두 하나로 본다)
def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)
    return True

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        if dfs(i):
            cnt += 1
print(cnt)