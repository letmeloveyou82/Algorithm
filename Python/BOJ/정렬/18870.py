import sys

input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
X_dict = dict()
idx = 0

for i in sorted(X):
    if X_dict.get(i) == None:
        X_dict[i] = idx
        idx += 1

result = []
for i in X:
    result.append(X_dict[i])
print(*result)
