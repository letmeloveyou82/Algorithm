import sys 

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_graph(parent, a, b):
    a_root = find_root(parent, a)
    b_root = find_root(parent, b)

    if a_root > b_root :
        parent[a_root] = b_root
    else:
        parent[b_root] = a_root

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] * (n)
answer = 0

for i in range(n):
    parent[i] = i
    
cycle = False

for i in range(1, m+1):
    a, b = map(int, input().split())
    
    if find_root(parent, a) == find_root(parent, b) and not cycle:
        cycle = True
        answer = i
    else:
        union_graph(parent, a, b)

print(answer)