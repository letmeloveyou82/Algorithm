import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 7개 좌표들이 서로 연결된 좌표인지 확인
def check(num):
    global available
    r = num // 5
    c = num % 5
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
            continue
        next_num = nr*5+nc # 다음 숫자
        if next_num in p: # p에 있다면 방문표시, 재귀로 다음 숫자 넘겨 재검사
            visited[nr][nc] = 1
            available+=1
            check(next_num)

# (depth, 'Y'의 개수, 사용할 숫자 인덱스)
def dfs(depth, y_count, idx):
    global result, available, visited
    if y_count > 3 or 25-idx < 7-depth: # 가지치기
        return
    if depth == 7: # depth가 7에 도달하면 연결 여부 검사
        available = 1 # 연결된 좌표 갯수
        visited = [[0] * 5 for _ in range(5)]
        sr, sc = p[0]//5, p[0]%5 # 5*5 맵 좌표로 변환
        visited[sr][sc] = 1 # 시작 위치 표시
        check(p[0]) # 연결된 좌표인지 확인
        if available == 7: # 7개 좌표가 연결됐다면 +1 
            result += 1
        return
    r = idx // 5
    c = idx % 5
    if girls[r][c] == "Y": # "Y"이면 y_count + 1
        p.append(idx)
        dfs(depth+1, y_count+1, idx+1)
        p.pop()
    else: # "S"이면 그냥 넘기기
        p.append(idx)
        dfs(depth+1, y_count, idx+1)
        p.pop()
    dfs(depth, y_count, idx+1) # 사용하지 않고, 그냥 인덱스만 넘긴다!

girls = [input().rstrip() for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
result = 0
p = []
dfs(0, 0, 0)
print(result)
    