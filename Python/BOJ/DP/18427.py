n, m, h = map(int, input().split())
dp = [[1] + [0]*h for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = dp[i-1][:] # dp[i-1]를 얕은 복사하여 dp[i]에 저장
    blocks = list(map(int, input().split()))
    for b in blocks:
        for j in range(b, h+1):
            dp[i][j] += dp[i-1][j-b]
print(dp[n][h]%10007)