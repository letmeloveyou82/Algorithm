import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 1번째 BFS(육지마다 번호 붙여 구분)
def bfs(r, c, num):
    q = deque()
    graph[r][c] = num
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = num
                    q.append((nx, ny))
    return

# 2번째 BFS(최단거리 구하기)
def make_bridge(num):
    q = deque()
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<N and 0<=ny<N:
                # 바다가 아니고 다른 육지를 만났다면
                if graph[nx][ny] != 0 and graph[nx][ny] != num:
                    return dist[x][y]
                # 바다이고 아직 다리가 없다면
                elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append([nx, ny])

    return int(1e9)

num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j, num)
            num += 1

result = int(1e9)
for v in range(2, 2+N):
    result = min(result, make_bridge(v))
print(result)