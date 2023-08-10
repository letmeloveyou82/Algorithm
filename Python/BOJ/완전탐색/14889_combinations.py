# combinations 사용
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
members = list(range(n))
min_value = int(1e9)

for r1 in combinations(members, n//2):
    start, link = 0, 0
    r2 = list(set(members) - set(r1))
    for r in combinations(r1, 2):
        start += board[r[0]][r[1]]
        start += board[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += board[r[0]][r[1]]
        link += board[r[1]][r[0]]
    min_value = min(min_value, abs(start-link))
print(min_value)