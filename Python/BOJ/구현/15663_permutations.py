# permutations 사용
from itertools import permutations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))

new_num = list(set(permutations(num, m)))
new_num.sort()
for i in new_num:
    print(*i)
