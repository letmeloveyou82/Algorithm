def solution(board, h, w):
    n = len(board)
    cnt = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n:
            if board[h][w] == board[nh][nw]:
                cnt += 1
    return cnt