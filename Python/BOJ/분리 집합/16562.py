import sys

input = sys.stdin.readline
N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
parents = [i for i in range(N+1)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    if A[a_parent] < A[b_parent]:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

friends = set()
cost = 0
for i in range(1, N+1):
    if find(i) not in friends:
        cost += A[parents[i]]
        friends.add(parents[i])

if cost > k:
    print("Oh no")
else:
    print(cost)
