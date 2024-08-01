import sys
from collections import deque

def bfs(start):
    visited = [False] * (N+1)
    cnt = 0
    q = deque()
    q.append([0, start])
    visited[start] = True
    while q:
        dist, x = q.popleft()
        if cnt < dist:
            cnt = dist
        for next_node in graph[x]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append([dist+1, next_node])
    return cnt

input= sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
president_score = int(1e9)
president_candidate = []
answer = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    score = bfs(i)
    if score < president_score:
        president_score = score
    president_candidate.append(score)

for i in range(N):
    if president_candidate[i] == president_score:
        answer.append(i+1)

print(president_score, len(answer))
print(*answer)
