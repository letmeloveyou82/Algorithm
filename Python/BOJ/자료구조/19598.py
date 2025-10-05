import sys, heapq

input = sys.stdin.readline

N = int(input())
meeting_time = [list(map(int, input().split())) for _ in range(N)]
end_time = []
meeting_time = sorted(meeting_time, key=lambda x : x[0])
heapq.heappush(end_time, meeting_time[0][1])
i = 1

while i < N:
    end = heapq.heappop(end_time)
    # 끝나는 시간이 그 다음 시작 시간보다 크면 회의실 추가해줘야 됨
    if meeting_time[i][0] < end:
        heapq.heappush(end_time, end)
    heapq.heappush(end_time, meeting_time[i][1])
    i += 1

print(len(end_time))