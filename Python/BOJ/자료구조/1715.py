import sys, heapq

input = sys.stdin.readline
N = int(input())
card_heap = []
for _ in range(N):
    heapq.heappush(card_heap, int(input()))

total = 0
while len(card_heap) > 1:
    a = heapq.heappop(card_heap)
    b = heapq.heappop(card_heap)
    sum_card = a+b
    total += sum_card
    heapq.heappush(card_heap, sum_card)
print(total)
