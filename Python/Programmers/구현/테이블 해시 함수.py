def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x : (x[col-1], -x[0]))

    for i in range(row_begin, row_end+1):
        s = 0
        for k in data[i-1]:
            s += k % i
        answer ^= s # 누적 XOR 연산
    
    return answer