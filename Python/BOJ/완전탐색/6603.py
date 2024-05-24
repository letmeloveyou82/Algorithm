import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    result = []
    for i in combinations(l[1:], 6):
        result.append(i)
    result.sort()
    for i in result:
        print(*i)
    print()