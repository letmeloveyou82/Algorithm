import sys
from collections import deque

def game():
    time = 0
    now_dir_idx = 0
    while True:
        time += 1
        # 뱀은 몸 길이를 늘려, 머리를 다음칸에 위치시킨다.
        nx = snake[0][0] + dx[now_dir_idx%4]
        ny = snake[0][1] + dy[now_dir_idx%4]
        snake.appendleft([nx, ny])
        # 만약 벽이나 자기 자신의 몸과 부딪히면 게임이 끝난다.
        if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 1:
            return time
        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[nx][ny] == 2:
            board[nx][ny] = 0
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워둔다.
        else:
            board[snake[-1][0]][snake[-1][1]] = 0
            snake.pop()
        board[nx][ny] = 1 # board에 뱀의 머리 위치 저장
        
        # x초가 끝난 후에 c 방향으로 90도 회전한다.
        if len(snake_dir_change) != 0:
            if snake_dir_change[0][0] == time:
                x, c = snake_dir_change.popleft()
                if c == 'L':
                    now_dir_idx += 3
                else:
                    now_dir_idx += 1

input = sys.stdin.readline
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = 1 # 뱀 위치 1로 표시

snake_dir_change = deque()
for _ in range(K):
    R, C = map(int, input().split())
    board[R-1][C-1] = 2 # apple 위치 2로 표시
    
L = int(input())
for _ in range(L):
    X, C = input().split()
    # X초 끝난 뒤 90도 방향 회전하는데 L이면 왼쪽, D이면 오른쪽
    snake_dir_change.append([int(X), C])

snake = deque([[0, 0]])

# 오른쪽으로 90도 방향 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(game())