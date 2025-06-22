import sys
input = sys.stdin.readline

N = int(input())
MOD = 10007
dp = [[0] * 10 for _ in range(N+1)]

# 초기화
for j in range(10):
    dp[1][j] = 1

# 누적합 점화식 적용
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(10):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(sum(dp[N]) % MOD)
