def solution(n, money):
    dp = [0] * (n+1)
    for m in money:
        dp[m] += 1
        for j in range(n+1):
            if j-m > 0:
                dp[j] += dp[j-m]
    return dp[n] % 1000000007