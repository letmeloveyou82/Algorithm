import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
card = []
for value in list(map(int, input().split())):
    heapq.heappush(card, value)
for _ in range(m):
    sum = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, sum)
    heapq.heappush(card, sum)
result = 0
for i in card:
    result += i
print(result)