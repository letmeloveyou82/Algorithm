T = int(input())
for test_case in range(1, T+1):
    result = "Possible"
    N, M, K = map(int, input().split())
    arrived = list(map(int, input().split()))
    arrived.sort()
    for i in range(N):
        if arrived[0] < M:
            result = "Impossible"
            break
        now_K = arrived[i] // M * K
        if i + 1 > now_K:
            result = "Impossible"
            break
    print(f"#{test_case} {result}")