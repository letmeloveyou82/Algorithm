from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 컨베이어 벨트의 길이, 종료 조건 k
durability = deque() # 내구도
for i in map(int, input().split()):
    durability.append(i)
robot = deque([0] * (n)) # 로봇 위치
count = 0
while True:
    if durability.count(0) >= k: # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
        break
    count += 1
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    durability.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 # 로봇이 내리는 위치에 도달하면 즉시 내림
    # 가장 먼저 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    if sum(robot):
        for i in range(n-2, -1, -1): # 로봇 내려가는 부분 인덱스 i-1이므로 그 전인 i-2부터
            if robot[i] == 1 and robot[i+1] == 0 and durability[i+1] >=1 :
                robot[i+1] = 1
                robot[i] = 0
                durability[i+1] -= 1
        robot[-1] = 0 # 로봇이 내리는 위치에 도달하면 즉시 내림
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if durability[0] >= 1 and robot[0] == 0:
        robot[0] = 1
        durability[0] -= 1
print(count)