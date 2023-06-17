import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []
end_time = []
count = 0
for _ in range(n):
    lec_num, start, end = map(int, input().split())
    heapq.heappush(heap, [start, end, lec_num])

start, end, num = heapq.heappop(heap)
heapq.heappush(end_time, end)
while heap:
    start, end, num = heapq.heappop(heap)
    if end_time[0] <= start:
        heapq.heappop(end_time)
    heapq.heappush(end_time, end)
print(len(end_time))