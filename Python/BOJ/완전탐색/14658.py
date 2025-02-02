import sys

input = sys.stdin.readline
N, M, L, K = map(int, input().split())
shooting_star = [tuple(map(int, input().split())) for _ in range(K)]
ans = 0

for fx, fy in shooting_star:
    for sx, sy in shooting_star:
        stars = 0
        for px, py in shooting_star:
            if fx <= px <= fx + L and sy <= py <= sy + L:
                stars += 1
        ans = max(ans, stars)
print(K - ans)