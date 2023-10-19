import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, r = map(int, input().split())
graph =[[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [0] * (n+1)
cnt = 1
def dfs(r):
    global cnt
    visited[r] = cnt 
    graph[r].sort() # 정점 번호를 오름차순으로 방문
    for i in graph[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)
for i in range(1, n+1):
    print(visited[i])