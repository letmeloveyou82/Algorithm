import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
result = int(1e9)
prefix_sum = [0] * (N+1)

# 누적합 계산
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + num[i-1]

# 투 포인터
left, right = 0, 0
while left < N+1:
    if right == N+1:
        left += 1
    elif prefix_sum[right] - prefix_sum[left] >= S:
        result = min(result, right-left)
        left += 1
    else:
        right += 1
if result == int(1e9):
    print(0)
else:
    print(result)