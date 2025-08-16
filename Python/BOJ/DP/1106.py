import sys
input = sys.stdin.readline

C, N = map(int, input().split())
promotions = [[0, 0]]
for i in range(N):
    price, customer = map(int, input().split())
    promotions.append([price, customer])
    
result = float('inf')
dp = [result for _ in range(C+100)]
dp[0] = 0

for i in range(1, N+1):
    price, customer = promotions[i]
    for j in range(customer, C+100):
        dp[j] = min(dp[j], dp[j-customer]+price)

print(min(dp[C:]))