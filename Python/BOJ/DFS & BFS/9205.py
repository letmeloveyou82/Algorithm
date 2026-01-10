import sys
from collections import deque

input = sys.stdin.readline

def can_go(points, n):
    # points: 집 + 편의점 n개 + 페스티벌 위치
    
    q = deque([0])
    visited = [False] * (n+2)
    visited[0] = True
    
    while q:
        idx = q.popleft()
        if idx == n+1: # festival 인덱스
            return True

        x, y = points[idx]
        for next in range(n+2):
            if not visited[next]:
                nx, ny = points[next]
                if abs(x-nx)+abs(y-ny) <= 1000:
                    visited[next] = True
                    q.append(next)

    return False

for _ in range(int(input())):
    n = int(input())
    points = [tuple(map(int, input().split()))]
    for _ in range(n+1):
        points.append(tuple(map(int, input().split())))

    print("happy" if can_go(points, n) else "sad")