n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
count = 0
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True  # 방문처리
    if graph[x][y] == '-':
        if y+1 < m and graph[x][y+1] == '-' and visited[x][y+1] == False: # 좌우 확인
            dfs(x, y+1)
        else:
            return
    if graph[x][y] == '|':
        if x+1 < n and graph[x+1][y] == '|' and visited[x+1][y] == False: # 상하 확인
            dfs(x+1, y)
        else:
            return

for i in range(n):
    for j in range(m):
        if visited[i][j] == False: # 방문하지 않았다면 dfs 수행
            dfs(i, j)
            count += 1
print(count)
