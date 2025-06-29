import sys

input = sys.stdin.readline
N, M, P = map(int, input().split())
dp = [[0]*(P+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, P+1):
    for j in range(1, N+1):
        dp[j][i] += dp[j-1][i-1] * (N-(j-1))
        if j > M :
            dp[j][i] += dp[j][i-1] * (j-M)
        dp[j][i] %= 1000000007

print(dp[N][P])