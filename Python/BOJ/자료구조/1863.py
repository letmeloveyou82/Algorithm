import sys

input = sys.stdin.readline
n = int(input())
stack = []
answer = 0

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    while stack and stack[-1] > y:
        answer += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)

while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)