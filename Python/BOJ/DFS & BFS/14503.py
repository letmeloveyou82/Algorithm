from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 청소기가 바라보는 방향(북 0, 동 1, 남 2 , 서 3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계 방향으로 90도 회전
def turn_left(d):
    d -= 1
    if d == -1:
        d = 3
    return d

# BFS
def bfs(x, y, d):
    clean = 1 # 처음 빈 칸 청소
    q = deque() 
    q.append((x, y, d))
    graph[x][y] = 2 # 청소 완료는 2로 표시

    while q:
        x, y, d = q.popleft()
        nd = d
        # 현재 위치에서 4 방향으로의 위치 확인
        for i in range(4):
            # 왼쪽 영역 탐색
            nd = turn_left(nd)
            nx = x + dx[nd]
            ny = y + dy[nd]
            # 가능한 칸 중 청소되지 않은 빈 칸이 있는 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                clean += 1 
                graph[nx][ny] = 2
                q.append((nx, ny, nd))
                break
            # 가능한 칸 중 청소되지 않은 빈 칸이 없는 경우 한 칸 후진
            elif i == 3:
                if d == 0:
                    x += 1
                elif d == 1:
                    y -= 1
                elif d == 2:
                    x -= 1
                elif d == 3:
                    y += 1
                q.append((x, y, d))
                if graph[x][y] == 1: # 벽이라 후진할 수 없다면 작동 멈춤
                    return clean

print(bfs(r, c, d))