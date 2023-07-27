from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, costs):
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    queue.append((nx, ny))
num = 1
while True:
    n = int(input())
    if n == 0:
        exit()
    else:
        graph = [list(map(int, input().split())) for _ in range(n)]
        costs = [[int(1e9)] * n for _ in range(n)]
        costs[0][0] = graph[0][0]
        bfs(graph, costs)
        print(f"Problem {num}: {costs[n-1][n-1]}")
        num += 1