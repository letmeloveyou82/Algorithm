from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
graph = []
q = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1: # 익은 토마토 위치를 큐에 넣음
            q.append((i,j))

# 갈 수 있는 4 방향 정의 (왼, 오, 앞, 뒤)
directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs():
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft()
        # 현재 위치에서 갈 수 있는 주변 4방향 확인
        for i in range(4): 
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: # 익지 않은 토마토인 경우
                q.append((nx, ny)) 
                graph[nx][ny] = graph[x][y] + 1 
bfs()
day = 0
for line in graph:
    for t in line:
        if t == 0: # 익지 않은 토마토가 있는 경우
            print(-1) # -1 출력
            exit(0) # 종료
print(max(map(max, graph))-1) # 익지 않은 토마토가 없으면 최대값 출력하는데 처음을 1로 시작했으니 -1 빼줌