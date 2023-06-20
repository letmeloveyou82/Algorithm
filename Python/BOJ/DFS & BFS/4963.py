import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4) # 파이썬 재귀깊이 제한 해제 원래 1000인데 10000으로 수정

# 8방향 정의
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y, graph):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or y<=-1 or x>=h or y>=w or graph[x][y] == 0:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 2
        # 8 방향 모두 재귀적으로 호출 
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, graph)
        return True
    return False

def land_count(h, w, graph):
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph) == True:
                count += 1
    print(count)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        graph = []
        for i in range(h):
            graph.append(list(map(int, input().split())))
        land_count(h, w, graph)
