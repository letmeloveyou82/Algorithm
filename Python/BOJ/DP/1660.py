import sys
input = sys.stdin.readline

N = int(input())

# N이하 사면체수 목록 만들기
i = 1
tri = 0 # 한 층마다
tetra = 0 # 사면체 수
case = []
while True:
    tri += i
    tetra += tri
    if tetra > N:
        break
    case.append(tetra)
    i += 1

# 합을 N으로 만들 때의 필요한 최소 개수
INF = float('inf')
dp = [INF] * (N+1)
dp[0] = 0

for c in case: # 사용할 수 있는 사면체수 하나씩
    for s in range(c, N+1): # 합을 만들 때
        if dp[s-c] + 1 < dp[s]:
            dp[s] = dp[s-c]+1

print(dp[N])