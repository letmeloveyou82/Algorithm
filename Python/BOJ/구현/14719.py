import sys
input = sys.stdin.readline
h, w = map(int, input().split())
block = list(map(int, input().split()))

m = 0
for i in range(w):
    if m < block[i]:
        max_idx = i
        m = block[i]
now = 0
roof = 0

for i in range(max_idx+1): # 왼쪽 그룹
    now = max(now, block[i])
    roof += now
now = 0
for i in range(w-1, max_idx, -1): # 오른쪽 그룹
    now = max(now, block[i])
    roof += now

# 블록 총 넓이
area = 0
for i in range(w):
    area += block[i]

print(abs(roof-area))