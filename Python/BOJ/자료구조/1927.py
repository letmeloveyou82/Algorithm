import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))