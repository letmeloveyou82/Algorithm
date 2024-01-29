import sys
input = sys.stdin.readline
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x:(x[1], x[0]))

ans = end = 0
for s, e in meeting:
    if s >= end:
        ans += 1
        end = e
print(ans)