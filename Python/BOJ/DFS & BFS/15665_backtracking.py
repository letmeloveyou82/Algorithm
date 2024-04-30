import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
nums_without_dupli = []
for num in numbers:
    if num not in nums_without_dupli:
        nums_without_dupli.append(num)
tmp = []

def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(start, len(nums_without_dupli)):
        tmp.append(nums_without_dupli[i])
        dfs(start)
        tmp.pop()

dfs(0)