node = int(input())
edge = int(input())
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (node + 1)
cnt = 0

# 1번 노드와 연결된 노드 개수 탐색
def dfs(x):
  global cnt
  for i in graph[x]:
    if visited[i] == 0:
      visited[i] = 1
      cnt += 1
      dfs(i)
  return

visited[1] = 1
dfs(1)
print(cnt)