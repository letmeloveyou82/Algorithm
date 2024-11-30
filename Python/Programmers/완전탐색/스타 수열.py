from collections import Counter
def solution(a):
    elements = Counter(a)
    answer = -1
    
    for key in elements.keys():
        if elements[key] <= answer:
            continue
        idx = 0
        cnt = 0
        
        while idx < len(a)-1:
            if (a[idx] != key) and (a[idx+1] != key): # 교집합이 생기지 않음
                idx += 1
                continue
            if a[idx] == a[idx+1]: # x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1] 조건에 위배됨
                idx += 1
                continue
            cnt += 1
            idx += 2
        answer = max(answer, cnt)
        
    if answer == -1:
        return 0
    else:
        return answer*2