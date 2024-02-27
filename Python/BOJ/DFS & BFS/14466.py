import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K, R = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
road = defaultdict(list)
visited = [[0] for _ in range(N) for _ in range(N)]
cow = set()

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[(r1-1, c1-1)].append((r2-1, c2-1))
    road[(r2-1, c2-1)].append((r1-1, c1-1))

for _ in range(K):
    r, c = map(int, input().split())
    cow.add((r-1, c-1))

def bfs(q):
    global visited
    pair_cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in road[(x, y)] and not visited[nx][ny]:
                if (nx, ny) in cow:
                    pair_cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return K - pair_cnt

not_pair_cnt = 0
q = deque()
for x, y in cow:
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    q.append((x, y))
    not_pair_cnt += bfs(q)

print(not_pair_cnt//2)