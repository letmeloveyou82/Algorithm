import sys
input = sys.stdin.readline
n = int(input()) # 두 전봇대 사이의 전깃줄의 개수
wire = []
dp = [1] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    wire.append([a,b])
wire.sort() # 오름차순 정렬

# b 전봇대에서 가장 긴 증가하는 부분수열 구하기
for i in range(1, n):
    for j in range(0, i):
        if wire[j][1] < wire[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
