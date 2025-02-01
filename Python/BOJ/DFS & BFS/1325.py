# PyPy3
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

# A가 B를 신뢰한다. = B를 해킹하면, A도 해킹 가능
# B -> A
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

result = [-1]
for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    cnt = 1
    q = deque([i])
    while q:
        x = q.popleft()
        for next in graph[x]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
                cnt += 1
    result.append(cnt)

max_num = max(result)
max_lst = []
for i in range(1, N+1):
    if result[i] == max_num:
        max_lst.append(i)
print(*max_lst)