import sys
input = sys.stdin.readline

N = int(input())
t = [0] * (N+1)
p = [0] * (N+1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1]) # 이전까지의 최댓값
    finish_date = i + t[i] - 1 # i일에 해당하는 상담이 끝나는 시점
    if finish_date <= N: # 최종일 안에 상담이 끝나면
        dp[finish_date] = max(dp[finish_date], dp[i-1]+p[i])

print(max(dp))