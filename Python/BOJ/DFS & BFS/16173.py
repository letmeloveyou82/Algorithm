import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, graph):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == -1:
        visited[x][y] = 1
        return True
    can_go = graph[x][y]
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x+can_go, y, graph)
        dfs(x, y+can_go, graph)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dfs(0, 0, graph)

if visited[n-1][n-1] == 1:
    print("HaruHaru")
else:
    print("Hing")
