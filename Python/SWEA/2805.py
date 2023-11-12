T = int(input())
for test_case in range(1, T+1):
    result = 0
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    for r1 in range(N//2+1):
        for j in range(mid-r1, mid+r1+1):
            result += farm[r1][j]
    for r2 in range(N//2+1, N):
        cnt = N-1 - r2
        for j in range(mid-cnt, mid+cnt+1):
            result += farm[r2][j]

    print(f'#{test_case} {result}')