import sys
from collections import deque

input = sys.stdin.readline
N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)] # 방문처리 리스트가 3차원
min_time = T+1
q = deque()

def bfs():
    global min_time
    
    q.append((0, 0, 0, 0)) # x, y, time, sword
    visited[0][0][0] = True

    while q:
        x, y, time, sword = q.popleft()
        if time > T:
            continue
        if x == N-1 and y == M-1:
            if time < min_time:
                min_time = time
                continue
                
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if sword == 1:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.append([nx, ny, time + 1, 1])
                else:
                    if castle[nx][ny] == 0 and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        q.append((nx, ny, time + 1, 0))
                    elif castle[nx][ny] == 2 and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.append((nx, ny, time + 1, 1))

bfs()
print(min_time if min_time <= T else "Fail")