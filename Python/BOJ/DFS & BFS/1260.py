import sys
from collections import deque

input = sys.stdin.readline
node, edge, start_node = map(int, input().split())
visited = [False] *(node+1)
visited2 = [False] *(node+1)
graph = [[] for _ in range(node+1)]
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    # 큐(Queue) 구현을 위해 deque 라이브러리르 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited2[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(start_node)
print()
bfs(start_node)