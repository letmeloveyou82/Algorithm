import copy
def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns+1) for _ in range(rows+1)]
    num = 1
    
    # 행렬 초기화
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i][j] = num
            num += 1  

    new_matrix = copy.deepcopy(matrix)
    
    for x1, y1, x2, y2 in queries:
        # 오른쪽, 아래, 왼쪽, 위
        move = [[0, 1, y2-y1], [1, 0, x2-x1], [0, -1, y2-y1], [-1, 0, x2-x1]]
        now_x, now_y = x1, y1
        min_value = int(1e9)
        
        for dx, dy, m in move:
            for i in range(1, m+1):
                original_x, original_y = now_x+(dx*(i-1)), now_y+(dy*(i-1))
                original_value = matrix[original_x][original_y] # 기존 값
                
                if original_value < min_value: # 최솟값 갱신
                    min_value = original_value
                    
                nx, ny = now_x+(dx*i), now_y+(dy*i) # 이동할 위치
                new_matrix[nx][ny] = original_value
                
            now_x, now_y = nx, ny # 방향 바꾸기 전 현재 위치 갱신
        
        # 회전한 부분만 기존 matrix에 적용
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                matrix[i][j] = new_matrix[i][j]

        answer.append(min_value)
    return answer