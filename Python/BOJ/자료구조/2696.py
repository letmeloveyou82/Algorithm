import sys
import heapq
input =sys.stdin.readline
T = int(input())

for _ in range(T):
    M = int(input())
    num = []
    for _ in range(M//10+1):
        num = num + list(map(int, input().split()))

    # 우선순위 큐 2개 사용
    min_heap = []
    max_heap = []
    result = [num[0]]
    mid = num[0]

    for idx, val in enumerate(num[1:]):
        if val > mid:
            heapq.heappush(min_heap, val)
        else:
            heapq.heappush(max_heap, (-val, val))

        if idx % 2 == 1:
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, (-mid, mid))
                mid = heapq.heappop(min_heap)
            elif len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, mid)
                mid = heapq.heappop(max_heap)[1]
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        print(result[i], end=" ")
        if (i+1) % 10 == 0:
            print()
