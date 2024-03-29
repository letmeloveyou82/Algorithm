import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    nearby_water_q = deque()

    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not graph[nx][ny]:
                    cnt += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if cnt > 0 :
            nearby_water_q.append((x, y, graph[x][y] - cnt))

    while nearby_water_q:
        x, y, tmp = nearby_water_q.popleft()
        graph[x][y] = max(0, tmp)
    return 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ice = []
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            ice.append((i, j)) # 빙산 위치를 (i, j) 형태로 ice에 저장

year = 0
while ice:
    group = 0
    del_list = []
    visited = [[0] * M for _ in range(N)]
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0: # 탐색이 끝나면 바다가 된 빙산 체크
            del_list.append((i, j))
    if group > 1: # 빙산그룹 2개 이상이면 년 출력
        print(year)
        break

    # 다 녹은 빙산은 탐색할 필요가 없으므로 ice에서 제거
    ice = sorted(list(set(ice) - set(del_list)))
    year += 1

if group < 2:
    print(0)