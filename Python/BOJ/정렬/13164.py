import sys
input = sys.stdin.readline
n, k = map(int, input().split()) # n개의 원생, k개의 조
kids = list(map(int, input().split()))

costs = []

for i in range(n-1): # 원생들의 키 차이 저장
    costs.append(kids[i+1] - kids[i])
costs.sort(reverse=True) # 내림차순 정렬

print(sum(costs[k-1:]))
