def solution(board, moves):
    answer = 0            
    n = len(board)
    pick = []

    for move in moves:
        move -= 1
        for r in range(n):
            if board[r][move] != 0:
                if pick:
                    if pick[-1] == board[r][move]:
                        answer += 2
                        pick.pop()
                        board[r][move] = 0
                        break 
                pick.append(board[r][move])
                board[r][move] = 0
                break
                    
    return answer