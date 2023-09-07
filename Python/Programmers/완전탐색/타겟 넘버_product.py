# 중복순열
from itertools import product
def solution(numbers, target):
    answer = 0
    for c in list(product([1, -1], repeat=len(numbers))):
        check = 0
        for j in range(len(numbers)):
            check += c[j] * numbers[j]
        if check == target:
            answer += 1
    return answer