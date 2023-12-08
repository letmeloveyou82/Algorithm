import sys
input = sys.stdin.readline

n = int(input())
glass = [0] * 10001
for i in range(1, n+1):
    glass[i] = int(input())

dp = [0] * 10001
dp[1] = glass[1]
dp[2] = glass[1] + glass[2]
dp[3] = max(glass[1] + glass[3], glass[2] + glass[3], dp[2])
for i in range(4, n+1):
    dp[i] = max(dp[i-3] + glass[i-1] + glass[i], dp[i-2] + glass[i], dp[i-1])
    
print(max(dp))