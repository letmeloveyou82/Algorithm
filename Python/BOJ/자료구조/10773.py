import sys
input = sys.stdin.readline

K = int(input())
nums = []
for i in range(K):
    now = int(input())
    if now == 0 and nums:
        nums.pop()
        continue
    nums.append(now)

print(sum(nums))