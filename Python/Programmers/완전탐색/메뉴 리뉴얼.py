from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    course_list = []
    asc_order = []
    for o in orders:
        tmp = list(o)
        tmp.sort()
        asc_order.append(tmp)

    def course_make(cnt):
        order_dict = defaultdict(int)
        for i in range(len(asc_order)):
            for j in combinations(asc_order[i], cnt):
                order_dict[j] += 1
        if len(order_dict) == 0:
            return

        max_val = max(order_dict.values())
        for key in order_dict.keys():
            if order_dict[key] >= 2 and order_dict[key] == max_val:
                course_list.append(key)

    for i in course:
        course_make(i)
    
    answer = sorted(["".join(c) for c in course_list])
    return answer