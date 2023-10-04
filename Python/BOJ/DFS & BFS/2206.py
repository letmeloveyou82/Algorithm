import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 3차원 행렬을 통해 벽의 파괴 파악
# visited[x][y][0] : 벽 파괴하지 않음
# visited[x][y][1] : 벽 파괴함
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    while q:
        a, b, wall_break = q.popleft()

        # 끝 점에 도달하면 이동 횟수 출력
        if a == n-1 and b == m-1:
            return visited[a][b][wall_break]
        
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            # 맵을 벗어나면 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽 파괴기회 사용하지 않은 경우 
            if graph[nx][ny] == 1 and wall_break == 0:
                visited[nx][ny][1] = visited[a][b][wall_break] + 1
                q.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 한 번도 방문하지 않은 경우
            elif graph[nx][ny] == 0 and visited[nx][ny][wall_break] == 0:
                visited[nx][ny][wall_break] = visited[a][b][wall_break] + 1
                q.append((nx, ny, wall_break))
    # 불가능할 경우 -1 리턴
    return -1

print(bfs(0, 0, 0))