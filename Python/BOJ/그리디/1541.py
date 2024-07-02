import sys
input = sys.stdin.readline

expression = input().rstrip().split('-')
nums = []
for exp in expression:
    sum = 0
    tmp = exp.split('+')
    for j in tmp:
        sum += int(j)
    nums.append(sum)

n = nums[0]
for i in range(1, len(nums)):
    n -= nums[i]
print(n)