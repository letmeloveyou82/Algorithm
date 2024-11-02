import sys

input = sys.stdin.readline
T, W = map(int, input().split())
tree = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]

dp[1][0], dp[1][1] = tree[1]%2, tree[1]//2
for t in range(2, T+1):
    for w in range(W+1):
        j = tree[t] % 2 if w % 2 == 0 else tree[t]//2
        dp[t][w] = max(dp[t-1][0:w+1]) + j

print(max(dp[-1]))