import sys
from collections import deque

def bfs():
    q = deque()
    q.append([0, N])
    visited[N] = True
    while q:
        time, now = q.popleft()
        if now == K:
            return time
        for op in [now+1, now-1, now*2]:
            if 0 <= op <= 100000 and not visited[op]:
                visited[op] = True
                q.append([time+1, op])

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [False] * (100001)

print(bfs())