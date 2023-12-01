import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
MAX_VAL = int(1e9)
dp = [[[MAX_VAL]*3 for _ in range(M)] for _ in range(N)]
for x in range(N):
    if x == 0:
        for y in range(M):
            for d in range(3):
                dp[x][y][d] = board[x][y]
    else:
        for y in range(M):
            if y == 0: # ↘(2)로 오는 방향이 존재하지 않음
                dp[x][y][0] = min(dp[x-1][y+1][1], dp[x-1][y+1][2]) + board[x][y]
                dp[x][y][1] = dp[x-1][y][0] + board[x][y]
            elif y == M-1: # ↙(0)로 오는 방향이 존재하지 않음
                dp[x][y][1] = dp[x-1][y][2] + board[x][y]
                dp[x][y][2] = min(dp[x-1][y-1][0], dp[x-1][y-1][1]) + board[x][y]
            else:
                dp[x][y][0] = min(dp[x-1][y+1][1], dp[x-1][y+1][2]) + board[x][y]
                dp[x][y][1] = min(dp[x-1][y][0], dp[x-1][y][2]) + board[x][y]
                dp[x][y][2] = min(dp[x-1][y-1][0], dp[x-1][y-1][1]) + board[x][y]

answer = int(1e9)
for i in range(M):
    answer = min(min(dp[N-1][i]), answer)
print(answer)