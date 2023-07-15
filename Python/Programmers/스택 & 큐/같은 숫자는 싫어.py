def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if i == 0:
            answer.append(arr[i])
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i+1])
    return answer