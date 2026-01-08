def solution(park, routes):
    
    # 명령에 따라 이동
    def move(x, y, h, w, route):
        d, cnt = route.split()
        for _ in range(int(cnt)):
            nx, ny = x+op[d][0], y+op[d][1]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: # 벗어나는 경우
                return False
            if park[nx][ny] == 'X': # 장애물 만난 경우
                return False
            x, y = nx, ny # 현재 위치 이동
        
        return [x, y]
    
    x, y = 0, 0
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j # 시작 위치 갱신
    
    # 이동 방향 정의
    op = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    
    for route in routes:
        result = move(x, y, h, w, route)
        if not result :
            continue
        x, y = result[0], result[1] # 현재 위치 갱신
        
    return [x, y]