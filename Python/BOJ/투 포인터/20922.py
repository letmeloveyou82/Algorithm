import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

cnt = defaultdict(int)
l = 0
ans = 0

for r in range(N):
    cnt[a[r]] += 1

    # a[r]가 K 초과이면, 다시 K 이하가 될 때까지 L 이동
    while cnt[a[r]] > K:
        cnt[a[l]] -= 1
        l += 1

    ans = max(ans, r-l+1)

print(ans)