import sys
input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1] * (N+1)

# LIS(최장 증가 부분 수열)
for i in range(1, N+1):
    for j in range(1, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))