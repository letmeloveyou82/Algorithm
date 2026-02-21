import sys, heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
beer = [tuple(map(int, input().split())) for _ in range(K)] # 선호도, 도수

beer.sort(key=lambda x:x[1]) # 도수 오름차순 정렬

heap = []
sum_v = 0

for v, c in beer: # 선호도, 도수
    heapq.heappush(heap, v)
    sum_v += v

    # N개 초과면 가장 선호도 낮은 맥주 버림
    if len(heap) > N:
        sum_v -= heapq.heappop(heap)

    # 정확히 N개를 채운 상태에서 합이 M 이상이면 현재 c가 최소 간 레벨
    if len(heap) == N and sum_v >= M:
        print(c)
        sys.exit(0)

print(-1)