n = int(input())
tower = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
  while stack:
    if stack[-1][1] >= tower[i]:
      answer[i] = stack[-1][0] + 1
      break
    else:
      stack.pop()
  stack.append((i, tower[i])) # (인덱스, 탑의 높이)
print(" ".join(map(str, answer)))