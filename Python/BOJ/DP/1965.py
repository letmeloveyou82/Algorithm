import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))

dp = [1 for _ in range(n)] # 최소 자기 자신 1개

# dp[i] = i번째 상자를 마지막으로 선택했을 때 넣을 수 있는 최대 상자 개수

for i in range(n):
    for j in range(i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))