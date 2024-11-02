import sys
from collections import deque

def bfs(x, y, z):
    q = deque()
    q.append([x, y, z])
    d[x][y][z] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<L and 0<=ny<R and 0<=nz<C:
                if graph[nx][ny][nz] == 'E':
                    print(f"Escaped in {d[x][y][z]} minute(s).")
                    return
                if graph[nx][ny][nz] == '.' and d[nx][ny][nz] == 0:
                    d[nx][ny][nz] = d[x][y][z] + 1
                    q.append([nx, ny, nz])
    print("Trapped!")

input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = [[[] * C for _ in range(R)] for _ in range(L)]
    d = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        graph[i] = [list(input().rstrip()) for _ in range(R)]
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    bfs(i, j, k)