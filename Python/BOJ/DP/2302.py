import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 41
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

M = int(input())

result = 1
group = []
previous = 0

for _ in range(M):
    vip = int(input())
    group.append(vip - previous - 1)
    previous = vip
group.append(N-previous)

for i in group:
    if i != 0:
        result *= dp[i]

print(result)