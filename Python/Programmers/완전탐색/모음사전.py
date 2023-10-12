from itertools import product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    case = []
    for i in range(1, 6):
        for j in product(alpha, repeat = i):
            temp = ''
            for k in j:
                temp += k
            case.append(temp)
    case.sort()
    return case.index(word)+1