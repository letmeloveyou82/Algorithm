from itertools import combinations
N = int(input())
ingredient = []
for _ in range(N):
    S, B = map(int, input().split())
    ingredient.append([S,B])
gap = int(1e9)
if N == 1:
    print(abs(ingredient[0][0]-ingredient[0][1]))
else:
    for i in range(1, N+1):
        for l in list(combinations(ingredient, i)):
            sour_taste = 1
            bitter_taste = 0
            for S, B in l:
                sour_taste *= S
                bitter_taste += B
            check = abs(sour_taste - bitter_taste)
            if gap > check:
                gap = check
    print(gap)