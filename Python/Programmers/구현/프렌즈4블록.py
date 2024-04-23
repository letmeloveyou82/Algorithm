def solution(m, n, board):
    # 2x2 형태를 찾고, 존재한다면 disappear에 위치 추가해주는 함수
    def find_2x2(i, j, ch):
        cnt = 1
        for x, y in [[i+1, j], [i+1, j+1], [i, j+1]]:
            if x < 0 or y < 0 or x >= m or y >= n:
                return 
            if visited[x][y] or new_board[x][y] != ch:
                return 
            cnt += 1
        if cnt == 4:
            for x, y in [[i, j], [i+1, j], [i+1, j+1], [i, j+1]]:
                if (x, y) not in disappear:
                    disappear.add((x, y))
        return

    answer = 0
    new_board = []
    for i in range(m):
        new_board.append(list(board[i]))

    disappear = set()
    
    while True:
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and new_board[i][j] != '0':
                    visited[i][j] = 1
                    find_2x2(i, j, new_board[i][j])
                    
        # 게임 종료 조건
        if len(disappear) == 0:
            return answer
            
		# 2x2 형태 다 찾고나서 한꺼번에 사라지도록 한다.
        while disappear:
            x, y = disappear.pop()
            answer += 1
            new_board[x][y] = '0' # 빈칸 처리

		# 블록이 아래로 떨어져 '0'인 공간을 채운다.
        column_list = []
        for j in range(n):
            tmp = []
            cnt = 0
            for i in range(m):
                if new_board[i][j] != '0':
                    tmp.append(new_board[i][j])
                else:
                    cnt += 1
            column_list.append(['0'] * cnt + tmp)

        for i in range(m):
            for j in range(n):
                new_board[i][j] = column_list[j][i]

    return answer