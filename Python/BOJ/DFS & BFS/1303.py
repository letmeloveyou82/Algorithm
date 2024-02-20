import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
w_result, b_result = 0, 0

def bfs(i ,j, team):
    result = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == team and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                result += 1
    return result**2

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'W' and visited[i][j] == 0:
            w_result += bfs(i, j, 'W')
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            b_result += bfs(i, j, 'B')

print(w_result, b_result)