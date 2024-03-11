from itertools import permutations
N = int(input())
num = [i for i in range(1, N+1)]

for i in list(permutations(num, N)):
    print(*i)