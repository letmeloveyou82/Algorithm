def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        # 아래에서부터 max 따진다. i는 4 -> 3 -> 2 -> 1로 변함
        for j in range(len(triangle[i])-1): # j는 0부터 그 행 마지막 값까지
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
    return triangle[0][0]