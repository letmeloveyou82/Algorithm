# 시계방향
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def solution(grid):
    answer = []
    lr, lc = len(grid), len(grid[0])
    
    # 4방향 방문 기록 리스트 : 4 * r * c
    visited = [[[0]*4 for _ in range(lc)] for _ in range(lr)]
    
    # 모든 좌표에 대해 탐색
    for r in range(lr):
        for c in range(lc):
            for d in range(4):
                # 해당 좌표와 방향이 이미 사용된 경우 
                if visited[r][c][d]:
                    continue
                    
                cnt = 0
                nx, ny = r, c
                while visited[nx][ny][d] == 0:
                    visited[nx][ny][d] = 1
                    cnt += 1
                    if grid[nx][ny] == "S": # 방향 변경 없음
                        pass
                    elif grid[nx][ny] == "L": # 반시계방향
                        d = (d-1)%4
                    elif grid[nx][ny] == "R": # 시계방향
                        d = (d+1)%4
                    # 좌표 길이로 % 연산해서 격자 벗어난 경우에도 자리 찾아가도록 함 
                    nx = (nx+dx[d])%lr
                    ny = (ny+dy[d])%lc
                
                answer.append(cnt)
    answer = sorted(answer)
    return answer