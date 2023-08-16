import sys
input = sys.stdin.readline
stick = [0 for _ in range(1001)] # 기둥
m = 0
for _ in range(int(input())):
    L, H = map(int, input().split())
    stick[L] = H
    if m < H:
        max_idx = L
        m = H
now = 0
answer = 0
for i in range(max_idx+1): # 왼쪽 그룹
    now = max(now, stick[i])
    answer += now
now = 0
for i in range(1000, max_idx, -1): # 오른쪽 그룹
    now = max(now, stick[i])
    answer += now
print(answer)