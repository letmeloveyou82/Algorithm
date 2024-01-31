import sys
input = sys.stdin.readline

result = 0
N = int(input())
num = [0] + [int(input()) for _ in range(N)]
dp = [1] * (N+1)

# 가장 긴 증가하는 부분수열 찾기
for i in range(1, N+1):
    for j in range(1, i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)

# N - 가장 긴 증가하는 부분수열의 길이
print(N-max(dp))