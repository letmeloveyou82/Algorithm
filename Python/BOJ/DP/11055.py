N = int(input())
A = list(map(int, input().split()))

dp = A[:]

# LIS 
for i in range(1, N): # 뒤
    for j in range(i): # 앞
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))