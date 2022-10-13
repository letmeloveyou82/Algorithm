import sys
input = sys.stdin.readline

# 런타임 에러(RecursionError) 뜰 때 해결하는 코드
sys.setrecursionlimit(10**6) # 파이썬 재귀깊이 제한 해제 - 원래 1000인데 100만으로 수정

# 테스트 케이스 개수 입력받기
t = int(input())

# DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y, graph):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or y<=-1 or x>=m or y>=n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y, graph)
        dfs(x+1, y, graph)
        dfs(x, y-1, graph)
        dfs(x, y+1, graph)
        return True
    return False

# 모든 노드(위치)에 대하여 
def program(m, n, graph):
    result = 0
    for i in range(m):
        for j in range(n):
            # 현재 위치에서 DFS 수행
            if dfs(i, j, graph) == True:
                result += 1
    print(result)

for i in range(t):
    # 2차원 리스트의 맵 정보 입력받기
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    # 테스트 케이스마다 해답 도출하도록
    program(m, n, graph)