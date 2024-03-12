def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    j = 0
    for i in range(len(A)):
        if A[i] < B[j]:
            answer += 1
            j += 1
    return answer