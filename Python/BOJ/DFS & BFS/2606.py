from collections import deque
node = int(input())
edge = int(input())
graph = [[] for _ in range(node+1)]
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (node+1)

def bfs(start):
    result = -1
    # 큐(Queue) 구현을 위해 deque 라이브러리를 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼낼 때마다 +1
        v = queue.popleft()
        result += 1
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print(result)

bfs(1)
