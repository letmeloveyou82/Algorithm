import sys
import heapq
input = sys.stdin.readline

n = int(input()) # 아이들과 거점지를 방문한 횟수 n
heap = []
for _ in range(n):
    a = list(map(int, input().split()))
    if len(a) == 1 and a[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-1*heapq.heappop(heap))
    else:
        for idx in range(1, a[0]+1):
            heapq.heappush(heap, -a[idx])
