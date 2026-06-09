from collections import Counter

def solution(X, Y):
    answer = ''
    count_X, count_Y = Counter(X), Counter(Y)
    common_key = count_X.keys() & count_Y.keys()
    
    if not common_key:
        return "-1"
    elif len(common_key) == 1 and "0" in common_key:
        return "0"
    else:
        common_key = sorted(common_key, reverse=True)
        for i in range(len(common_key)):
            answer += common_key[i] * min(count_X[common_key[i]], count_Y[common_key[i]])

    return answer