import sys, heapq
from collections import deque

input = sys.stdin.readline

N = int(input())
courses = []
for _ in range(N):
    courses.append(list(map(int, input().split())))
courses = deque(sorted(courses))
priority_q = []
heapq.heappush(priority_q, courses.popleft()[1])

while courses:
    s, t = courses.popleft()
    earlyEndTime = heapq.heappop(priority_q)
    if s < earlyEndTime:
        heapq.heappush(priority_q, earlyEndTime)
    heapq.heappush(priority_q, t)

print(len(priority_q))