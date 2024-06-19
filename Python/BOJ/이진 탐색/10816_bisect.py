import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
answer = []

for i in range(M):
    answer.append(bisect_right(card, check[i]) - bisect_left(card, check[i]))

print(*answer)