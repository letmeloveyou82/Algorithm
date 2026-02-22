from math import gcd 

def solution(arrayA, arrayB):
    answer = 0
    # arrayA 전체 gcd 구하기
    gA = arrayA[0]
    for x in arrayA[1:]:
        gA = gcd(gA, x)
    
    # arrayB 전체 gcd 구하기
    gB = arrayB[0]
    for x in arrayB[1:]:
        gB = gcd(gB, x)

    # 배열의 모든 값 나눌 수 있는 수인지 판별 
    def ok(a, other):
        for x in other:
            if x % a == 0:
                return False
        return True

    if ok(gA, arrayB):
        answer = gA
    if ok(gB, arrayA):
        answer = max(answer, gB)
        
    return answer