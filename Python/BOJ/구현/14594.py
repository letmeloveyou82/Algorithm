import sys
input = sys.stdin.readline
n = int(input()) # 동아리방 개수
m = int(input()) # 빅-종빈빌런의 행동 횟수
break_down_wall = []
for i in range(m):
    x, y = map(int, input().split())
    break_down_wall.append((x,y))
def number_of_rooms():
    if m == 0:
        return print(n)
    else:
        wall = [i for i in range(1, n+1)]
        for x, y in break_down_wall:
            if x == 1 and y == n:
                return print("1")
            else:
                for j in range(x, y):
                    wall[j] = 0
        print(n - wall.count(0))
number_of_rooms()