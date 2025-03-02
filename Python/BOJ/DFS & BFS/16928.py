import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
info_dict = dict()

for _ in range(N + M):
    x, y = map(int, input().split())
    info_dict[x] = y

visited = [0] * 101
q = deque()
q.append(1)
visited[1] = 1
cnt = 0

while q:
    for _ in range(len(q)):
        x = q.popleft()
        if x == 100:
            print(cnt)
            exit(0)

        for i in range(1, 7):
            nx = x + i

            if nx <= 100 and visited[nx] == 0:
                visited[nx] = 1

                if nx in info_dict.keys():
                    visited[info_dict[nx]] = 1
                    q.append(info_dict[nx])

                else:
                    q.append(nx)
    cnt += 1