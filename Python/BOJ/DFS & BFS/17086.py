from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 8 방향 정의(북, 서, 북서, 동, 남, 남동, 북동, 남서)
dx = [-1, 0, -1, 0, 1, 1, -1, 1]
dy = [0, -1, -1, 1, 0, 1, 1, -1]

queue = deque()

# BFS
def bfs():
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 8 방향으로의 위치 확인
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 공간 벗어나면 무시
                continue
            if graph[nx][ny] == 0: # 빈칸인 경우
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny))

# 상어 위치를 queue에 넣음
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()
print(max(map(max, graph))-1) # 2차원 리스트 내에 [0] 인덱스 기준이 아닌 모든 1차원 원소 중 최댓값 구하기 위해 map 함수 사용