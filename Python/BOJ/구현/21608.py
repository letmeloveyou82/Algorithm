import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * (N+1) for _ in range(N+1)]
like_friends_dict = dict() # 학생의 번호를 key로, 좋아하는 학생의 번호를 value로 갖는 dict
seat_dict = dict() # 학생의 번호를 key로, 학생이 앉은 자리를 value로 갖는 dict
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한 명씩 자리 앉기
def decide_seat():
    friends = list(map(int, input().split()))
    like_friends_dict[friends[0]] = friends[1:]
		
	# 1. 비어있는 칸 중에서 좋아하는 학생 여러 명과 인접한 칸이 어딘지 저장한다.
    possible_seat = []
    val = [[0] * (N + 1) for _ in range(N + 1)]
    for like_friend in friends[1:]:
        if like_friend in seat_dict:
            x, y = seat_dict[like_friend]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 1 <= nx < N + 1 and 1 <= ny < N + 1 and board[nx][ny] == 0:
                    val[nx][ny] += 1
    max_val = max(map(max, val))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if val[i][j] == max_val and board[i][j] == 0:
                possible_seat.append([i, j, 0])

	# 2-1. 1을 만족하는 칸이 1개라면, 해당 위치에 앉는다.
    if len(possible_seat) == 1:
        r, c = possible_seat[0][0], possible_seat[0][1]
        board[r][c] = friends[0]
        seat_dict[friends[0]] = [r, c]
        return

	# 2-2. 1을 만족하는 칸이 여러 개라면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸에 앉는다. 
	# 3. 2-2를 만족하는 칸이 여러 개인 경우, 1순위는 행의 번호 작은 칸, 2순위는 열의 번호 작은 칸에 앉는다.
    for idx in range(len(possible_seat)):
        for i in range(4):
            nx, ny = possible_seat[idx][0] + dx[i], possible_seat[idx][1] + dy[i]
            if 1 <= nx < N + 1 and 1 <= ny < N + 1 and board[nx][ny] == 0:
                possible_seat[idx][2] += 1
    blank_check_list = [possible_seat[i][2] for i in range(len(possible_seat))]
    max_blank = max(blank_check_list)
    max_idx = blank_check_list.index(max_blank)
    board[possible_seat[max_idx][0]][possible_seat[max_idx][1]] = friends[0]
    seat_dict[friends[0]] = [possible_seat[max_idx][0], possible_seat[max_idx][1]]

for _ in range(N**2):
    decide_seat()

# 학생의 만족도 계산
answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        now_student = board[i][j]
        satisfaction = 0
        for d in range(4):
            nx, ny = i+dx[d], j+dy[d]
            if 1 <= nx < N + 1 and 1 <= ny < N + 1:
                if board[nx][ny] in like_friends_dict[now_student]:
                    satisfaction += 1
        if satisfaction == 1:
            answer += 1
        elif satisfaction == 2:
            answer += 10
        elif satisfaction == 3:
            answer += 100
        elif satisfaction == 4:
            answer += 1000
print(answer)