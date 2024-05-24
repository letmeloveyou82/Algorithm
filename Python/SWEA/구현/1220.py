for tc in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    column_list = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if board[j][i] != 0:
                tmp.append(board[j][i])
        column_list.append(tmp)
    for col in column_list:
        if len(col) == 1:
            continue
        for i in range(len(col)-1):
            if col[i] == 1 and col[i+1] == 2:
                result += 1
    print(f"#{tc} {result}")