import sys
input = sys.stdin.readline

bingo = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
         [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
         [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]

while True:
    data = input().rstrip()
    if data == 'end':
        break
    tmp = list(data)
    x_cnt = tmp.count('X')
    o_cnt = tmp.count('O')

    board = []
    for i in range(3):
        board.append(list(data[i*3:i*3+3]))

    winner = ""
    x_bingo = 0
    o_bingo = 0

    # 빙고 확인
    for b in bingo:
        has_bingo = True
        value_x, value_y = b[0][0], b[0][1]
        if board[value_x][value_y] == '.':
            continue
        for x, y in b:
            if board[x][y] != board[value_x][value_y]:
                has_bingo = False
                break
        if has_bingo:
            winner = board[value_x][value_y]
            if board[value_x][value_y] == "X":
                x_bingo += 1
            else:
                o_bingo += 1

    # 발생 가능한 상태인지 판별
    if x_cnt+o_cnt == 9:
        if x_cnt == 5 and o_cnt == 4 and o_bingo == 0:
            print("valid")
            continue
    else:
        if winner != "":
            if winner == "X" and x_cnt - o_cnt == 1 and o_bingo == 0:
                print("valid")
                continue
            elif winner == "O" and x_cnt == o_cnt and x_bingo == 0:
                print("valid")
                continue

    print("invalid")