from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(land):
    answer = 0
    n = len(land) # 세로
    m = len(land[0]) # 가로
    oil_num_dict = dict() # oil_num을 key로, 석유량을 value로 갖는 dict
    
    # 덩어리마다 oil num(2부터) 붙이기
    def bfs(start_x, start_y, num):
        cnt = 0
        q = deque()
        q.append((start_x, start_y))
        land[start_x][start_y] = num
        cnt += 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and land[nx][ny] == 1:
                    q.append((nx, ny))
                    land[nx][ny] = num
                    cnt += 1
        return cnt
    
    num = 2 
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                oil_num_dict[num] = bfs(i, j, num)
                num += 1
    
    # 뽑을 수 있는 가장 많은 석유량 계산            
    for j in range(m):
        oil_set = set()
        tmp = 0
        for i in range(n):
            if land[i][j] != 0:
                oil_set.add(land[i][j])
        for oil in oil_set:
            tmp += oil_num_dict[oil]
        if answer < tmp:
            answer = tmp
    return answer