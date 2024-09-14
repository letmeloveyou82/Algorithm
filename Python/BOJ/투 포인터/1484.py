G = int(input())

N, M = 100001, 100001
left, right = 1, 1
answer = []

while left < N and right < M:
    now = (left+right) * (left-right)
    if now == G:
        answer.append(left)
    if now < G:
        left += 1
        continue
    right += 1

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)