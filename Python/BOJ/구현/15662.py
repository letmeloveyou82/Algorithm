import sys
from collections import deque

def rotate_wheel(num, dir):
    turn_element = []
    num -= 1

    # num의 오른쪽
    for i in range(num+1, T):
        if wheel[i][6] != wheel[i-1][2]:
            turn_element.append(i)
        else:
            break

    # num의 왼쪽
    for j in range(num-1, -1, -1):
        if wheel[j][2] != wheel[j+1][6]:
            turn_element.append(j)
        else:
            break
        
    wheel[num].rotate(dir)
    for element in turn_element:
        wheel[element].rotate(-dir if (element-num) % 2 else dir)

input = sys.stdin.readline
T = int(input())
wheel = [deque(input().rstrip()) for _ in range(T)] # 0 : N극, 1 : S극
K = int(input()) # 회전 횟수
for _ in range(K):
    wheel_num, rotation_dir = map(int, input().split()) # 회전시킨 톱니바퀴 번호, 방향
    rotate_wheel(wheel_num, rotation_dir)

print(sum([int(wheel[i][0]) for i in range(T)]))