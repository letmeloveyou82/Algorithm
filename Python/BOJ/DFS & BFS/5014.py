# 1 ~ F층까지 있음
# S층에서 G층까지 가기 위해 눌러야 하는 버튼의 수의 최솟값 구하기
# U : 위로 U층을 가는 버튼
# D : 아래로 D층을 가는 버튼
from collections import deque
import sys

def bfs(now):
    q = deque([now])
    visited[now] = 1
    while q:
        x = q.popleft()
        if x == G:
            return count[G]
        for nx in [x+U, x-D]:
            if 1 <= nx <= F and not visited[nx]:
                visited[nx] = 1
                count[nx] = count[x] + 1
                q.append(nx)
    if count[G] == 0:
        return "use the stairs"

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
count = [0] * (F+1)

print(bfs(S))