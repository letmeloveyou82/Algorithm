import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
num = []

def dfs(i, j):
    global cnt
    if i < 0 or j < 0 or i >= N or j >= N:
        return False
    if board[i][j] == 1: # 집이 있다면
        cnt += 1
        board[i][j] = 0 # 방문처리
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True
    return False

cnt = 0
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort() # 오름차순
print(result)
for i in range(len(num)):
    print(num[i])