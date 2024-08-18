# PyPy3
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
order = [i for i in range(1, 9)]
result = 0

for x in permutations(order, 8):
    x = list(x)
    batter = x[:3] + [0] + x[3:] # 4번 타자는 1번 선수로 고정
    number, score = 0, 0
    for i in range(N):
        out = 0
        b1 = b2 = b3 = 0
        while out < 3:
            if game[i][batter[number]] == 0:
                out += 1
            elif game[i][batter[number]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif game[i][batter[number]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif game[i][batter[number]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif game[i][batter[number]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            number += 1
            if number == 9:
                number = 0
    result = max(result, score)
print(result)