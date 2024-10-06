import sys

input = sys.stdin.readline
N = int(input())
chain = sorted(list(map(int, input().split())))
tied_chains = 1

for c in chain:
    if tied_chains + c >= N:
        break
    else:
        tied_chains += c
        N -= 1

print(N-1)