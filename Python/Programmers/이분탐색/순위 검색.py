from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for i in range(len(info)):
        info[i] = info[i].split()
        condition = info[i][0:4]
        score = int(info[i][-1])
        # '-'일 때도 찾을 수 있게 16개의 조건을 key로, score를 values로 저장
        for j in range(5):
            for c in list(combinations([0, 1, 2, 3], j)):
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(score)
                
    for value in dic.values():
        value.sort() # 점수 오름차순 정렬
        
    for q in query:
        q = q.replace("and", "").split()
        target_key = ''.join(q[0:4])
        target_score = int(q[-1])
        cnt = 0
        if target_key in dic.keys():
            target_list = dic[target_key]
            # bisect_left는 lower bound(원하는 값 이상 처음 나오는 위치) 찾아서 반환
            idx = bisect_left(target_list, target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
            
    return answer