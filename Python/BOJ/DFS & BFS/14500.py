# 입력
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# DFS
def dfs(x, y, L, total):
    global res
    # 예외 처리
    if res >= total + max_pos*(4-L): # 지금 있는 값에 board에서 제일 큰 값을 4-L번 더해도 res보다 작으면 return
        return
    # 깊이를 4번 다 돌고 테트로미노가 완성되었을 때
    if L == 4:
        res = max(res, total) # max로 res를 갱신해준 후 return
        return 
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                if L == 2: # 테트로미노의 블럭이 2개만 연결된 상태라면
                    visit[nx][ny] = 1
                    dfs(x, y, L+1, total+board[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, L+1, total+board[nx][ny]) # 지금 서있는 두번째 블록에서 한번 더 돌 예정이기 때문에 이전좌표에 L에 1 추가해 돈다
                visit[nx][ny] = 0
            
# 준비
max_pos = max(map(max,board)) # board에 들어있는 칸의 최댓값
res = 0 # 결과 저장용
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visit[i][j] = 0
print(res)