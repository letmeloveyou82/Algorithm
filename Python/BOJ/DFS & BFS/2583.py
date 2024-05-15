import sys
from collections import deque

def bfs(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    graph[i][j] = 2 # 방문한 위치는 2로 변경
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 2 # 방문한 위치는 2로 변경
                cnt += 1
    return cnt

input = sys.stdin.readline
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            # 직사각형 내부는 1로 저장
            if graph[M-1-y][x] == 0:
                graph[M-1-y][x] = 1
                
answer = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            answer.append(bfs(i, j))
            
answer.sort()
print(len(answer))
print(*answer)
