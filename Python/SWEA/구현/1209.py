for _ in range(1, 11):
    test_case = int(input())
    num = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    row_sum = 0
    column_sum = 0
    diagonal_sum1 = 0 # 아래로 내려가는 대각선
    diagonal_sum2 = 0 # 위로 올라가는 대각선
    for i in range(100):
        row_sum = max(row_sum, sum(num[i]))
        temp = 0
        for j in range(100):
            temp += num[j][i]
            if i == j:
                diagonal_sum1 += num[i][j]
            elif i + j == 99:
                diagonal_sum2 += num[i][j]
        column_sum = max(column_sum, temp)
    result = max(row_sum, column_sum, diagonal_sum1, diagonal_sum2)
    print(f'#{test_case} {result}')