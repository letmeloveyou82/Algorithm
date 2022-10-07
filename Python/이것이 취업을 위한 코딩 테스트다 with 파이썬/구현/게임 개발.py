n,m = map(int, input().split())
x, y, d = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
location = [[0]*m for _ in range(n)]
location[x][y] = 1 # 방문한 칸은 1로 변경

# 맵 정보 저장
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서
# 0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_count = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    next_x = x + dx[d]
    next_y = y + dy[d]
    # 회전 후 아직 안 가봤고 육지칸이라면 한 칸 전진
    if location[next_x][next_y] == 0 and arr[next_x][next_y] == 0:
        location[next_x][next_y] = 1
        # 이동
        x = next_x
        y = next_y
        count+=1
        turn_count = 0
        continue
    # 가봤고 바다인 경우
    else:
        turn_count += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_count == 4:
        next_x = x - dx[d]
        next_y = y - dy[d]
        # 뒤로 갈 수 있다면 이동
        if arr[next_x][next_y] == 0:
            x = next_x
            y = next_y
        # 뒤가 바다로 막혀있는 경우
        else: 
            break
        turn_count = 0

print(count)