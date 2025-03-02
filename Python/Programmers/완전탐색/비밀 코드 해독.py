from itertools import combinations

def solution(n, q, ans):
    answer = 0
    case = list(combinations(range(1, n+1), 5))
    for i in case:
        possible = True
        for j in range(len(q)):
            if len(set(i) & set(q[j])) != ans[j]:
                possible = False
                break
        if possible:
            answer += 1
    return answer