import sys 
from itertools import combinations

def calculate_distance(h):
    global ans
    total = 0
    # 사람마다 어떤 병원과 가장 최소 거리인지 따지고 total에 더함
    for x1, y1 in people:
        minimum = float('inf')
        for x2, y2 in h:
            minimum = min(minimum, abs(x2-x1)+abs(y2-y1))
        total += minimum
        if ans < total:
            return False
    return total

input = sys.stdin.readline 
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
hospital = []
people = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            hospital.append((i, j))
        elif graph[i][j] == 1:
            people.append((i, j))

for c in combinations(hospital, m):
    total_sum = calculate_distance(c)
    if not total_sum:
        continue
    if total_sum < ans:
        ans = total_sum
        
if ans == float('inf'):
    print(0)
else:
    print(ans)