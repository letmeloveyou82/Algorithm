# 백트래킹 사용 
import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
min_value = sys.maxsize

def backTracking(depth, idx):
    global min_value
    if depth == n//2:
        ability1, ability2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    ability1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    ability2 += board[i][j]
        min_value = min(min_value, abs(ability1-ability2))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backTracking(depth+1, i+1)
            visited[i] = False

backTracking(0, 0)
print(min_value)
