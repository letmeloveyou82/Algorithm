import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
domino = [list(map(int, input().split())) for _ in range(N)]
result = [list('S' * M) for _ in range(N)]

# E, W, S, N 동서남북
dir = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

def attack(x, y, d):
    global score
    if result[x][y] == 'F':
        return
    q = deque()
    q.append((x, y))
    dx, dy = dir[d]
    while q:
        cx, cy = q.popleft()
        for i in range(domino[cx][cy]):
            nx, ny = cx + dx * i, cy + dy * i
            if 0 <= nx < N and 0 <= ny < M:
                if result[nx][ny] == 'S':
                    result[nx][ny] = 'F'
                    score += 1
                    q.append((nx, ny))


def defend(x, y):
    if result[x][y] == 'F':
        result[x][y] = 'S'

score = 0

for _ in range(R):
    attack_x, attack_y, attack_d = input().split()
    attack_x, attack_y = int(attack_x)-1, int(attack_y)-1
    defend_x, defend_y = map(int, input().split())
    defend_x, defend_y = defend_x-1, defend_y-1

    attack(attack_x, attack_y, attack_d)
    defend(defend_x, defend_y)

print(score)
for row in result:
    print(' '.join(row))
