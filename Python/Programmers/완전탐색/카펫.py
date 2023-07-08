def solution(brown, yellow):
    answer = []
    total_num = brown + yellow
    for i in range(1, total_num+1):
        if total_num % i == 0:
            answer.append([i, total_num//i])
    for r, c in reversed(answer):
        num = (r-2)*2+(c-2)*2
        if r >= c and num == brown-4:
            return r, c