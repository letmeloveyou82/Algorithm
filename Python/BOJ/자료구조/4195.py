# 유니온 파인드(Union Find) 활용 문제
import sys
input = sys.stdin.readline

# 원소가 어떤 집합에 있는지 찾는 find 함수
# x로 들어온 원소의 Root노드를 반환
def find(x):
    if parent[x] == x: #  Root인 경우 x를 반환
        return x
    else: # 아니면 Root를 찾아감
        p = find(parent[x])
        parent[x] = p
        return p

# x원소와 y원소를 합치는 union 함수
# y의 Root노드를 x로 한다.
def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])


for _ in range(int(input())):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)