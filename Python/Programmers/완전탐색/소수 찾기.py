from itertools import permutations
def solution(numbers):
    answer = 0
    case = []
    paper = list(numbers)
    for i in range(1, len(paper)+1):
        case += permutations(paper, i)
    case = set(case)

    num = set()
    for i in case:
        value = "".join(i).lstrip("0")
        if value != "" and int(value) >= 2:
            num.add(int(value))
            
    for i in num:
        is_prime_num = True
        for j in range(2, i):
            if i % j == 0:
                is_prime_num = False
                break
        if is_prime_num:
            answer += 1
    return answer