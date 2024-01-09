import sys

input = sys.stdin.readline
N, K = map(int, input().split())
num = list(map(int, input().split()))

max_length = 0
left, right = 0, 0
num_count = [0] * (max(num)+1)

while right < N:
    if num_count[num[right]] < K:
        num_count[num[right]] += 1
        right += 1
        max_length = max(max_length, right - left)
    else:
        num_count[num[left]] -= 1
        left += 1

print(max_length)