import sys

input = sys.stdin.readline
N, M = map(int, input().split())
knowing_truth = set(list(map(int, input().split()))[1:])
parties = []

for _ in range(M):
    parties.append(set(list(map(int, input().split()))[1:]))

for _ in range(M):
    for party in parties:
        if party & knowing_truth:
            knowing_truth = knowing_truth.union(party)

cnt = 0
for party in parties:
    if party & knowing_truth:
        continue
    cnt += 1
print(cnt)