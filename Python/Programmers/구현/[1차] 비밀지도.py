def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a12 = bin(a1|a2)[2:].zfill(n)
        a12 = a12.replace("1", "#").replace("0", " ")
        answer.append(a12)
    return answer