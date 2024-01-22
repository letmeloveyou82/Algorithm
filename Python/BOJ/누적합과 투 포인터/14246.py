import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
k = int(input())
cnt = 0
prefix_sum = [0] * (n + 1)

# 누적합 계산
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num[i - 1]

left, right = 0, 0
while left < n:
    if right == n:
        left += 1
    elif prefix_sum[right + 1] - prefix_sum[left] > k:
        cnt += n - right
        left += 1
    else:
        right += 1

print(cnt)