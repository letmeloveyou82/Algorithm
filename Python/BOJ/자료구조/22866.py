import sys
input = sys.stdin.readline

N = int(input())
building = list(map(int, input().split()))
cnt = [0] * (N+1) # i번째 건물이 볼 수 있는 다른 건물의 수

near = [[int(1e9), int(1e9)] for _ in range(N+1)] # [가장 가까운 건물번호, 가장 가까운 건물거리]
stack = []

# 각 건물에서 좌측으로 보이는 건물의 개수 계산
for i, height in enumerate(building, 1):
    while stack and stack[-1][1] <= height:
        stack.pop()

    if stack:
        cnt[i] += len(stack)
        dist = abs(stack[-1][0] - i) # 해당 건물 기준 가장 가까운 좌측건물과의 거리
        if dist < near[i][1]:
            near[i][0] = stack[-1][0]
            near[i][1] = dist
        elif dist == near[i][1] and stack[-1][0] < near[i][0]: # 거리는 같은데 건물 번호가 더 작은 경우
            near[i][0] = stack[-1][0]

    stack.append([i, height]) # [건물번호, 건물높이]

# 각 건물에서 우측으로 보이는 건물의 개수 계산
stack = []
for i, height in reversed(list(enumerate(building, 1))):
    while stack and stack[-1][1] <= height:
        stack.pop()

    if stack:
        cnt[i] += len(stack)
        dist = abs(stack[-1][0] - i) # 해당 건물 기준 가장 가까운 우측건물과의 거리
        if dist < near[i][1]:
            near[i][0] = stack[-1][0]
            near[i][1] = dist
        elif dist == near[i][1] and stack[-1][0] < near[i][0]: # 거리는 같은데 건물 번호가 더 작은 경우
            near[i][0] = stack[-1][0]

    stack.append([i, height]) # [건물번호, 건물높이]

for i in range(1, N+1):
    if cnt[i] > 0:
        print(cnt[i], near[i][0])
    else:
        print(0)