import heapq
import sys
input = sys.stdin.readline # 처음에 시간초과 나서 추가함
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x != 0 :
        heapq.heappush(heap, (abs(x), x)) # 절댓값을 기준으로 먼저 정렬되고, 그 값이 같을 경우 튜플의 두 번째 요소를 기준으로 두고 정렬 
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")