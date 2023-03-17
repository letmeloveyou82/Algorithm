import sys
sys.setrecursionlimit(100000) # 런타임 에러 떠서 재귀 깊이 제한 바꿔줌
input = sys.stdin.readline

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 즉시 종료
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == '#': # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 방문 처리
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False

t = int(input()) 
for _ in range(t):
    h, w = map(int, input().split())
    graph = []
    visited = [False] * (h*w + 1)
    result = 0
    for i in range(h):
        graph.append(list(input().rstrip()))
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True: # 현재 위치에서 DFS 수행
                result += 1
    print(result)