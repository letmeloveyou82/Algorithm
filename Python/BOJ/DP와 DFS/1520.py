import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
	# 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if x == M-1 and y == N-1:
        return 1

	# 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[x][y] > graph[nx][ny]:
            ways += dfs(nx, ny)

    dp[x][y] = ways # 메모이제이션(Memoization) 기법
    return dp[x][y]


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

print(dfs(0, 0))