import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1 # 0원으로 만드는 가지 수 1개
    for c in coin:
        for money in range(1, M+1):
            if money >= c: # 금액이 동전의 가치보다 크면
                dp[money] += dp[money-c] # 해당 dp는 금액 - 동전에 해당하는 dp합
    print(dp[M])