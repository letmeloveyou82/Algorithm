from collections import defaultdict

def add_element(str):
    d = defaultdict(int)
    for i in range(len(str)-1):
        if 65 <= ord(str[i].upper()) <= 90 and 65 <= ord(str[i+1].upper()) <= 90:
            d[str[i:i+2].upper()] += 1
            
    return d

def solution(str1, str2):
    A = add_element(str1)
    B = add_element(str2)
    
    intersection_cnt = 0
    union_cnt = 0
    
    if len(set(A) & set(B)) == 0 and len(set(A) | set(B)) == 0:
        return 65536
    
    for element in set(A) & set(B):
        intersection_cnt += min(A[element], B[element])
    for element in set(A) | set(B):
        union_cnt += max(A[element], B[element])
    
    return int(intersection_cnt/union_cnt*65536)