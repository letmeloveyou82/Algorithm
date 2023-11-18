T = int(input())
for test_case in range(1, T + 1):
    result = -1
    N = int(input())
    num = list(map(int, input().split()))
    
    # 1 ≤ i < j ≤ N 인 두 i, j에 대해
    for i in range(N - 1):
        for j in range(i + 1, N):
            # Ai x Aj 값이 단조 증가하는 수인지 확인
            check_num = num[i] * num[j]
            tmp_str = str(check_num)
            increasing_number = True

            for d in range(len(tmp_str) - 1, 0, -1):
                n1 = check_num // 10 ** d
                check_num = check_num % 10 ** d
                n2 = check_num // 10 ** (d - 1)
                if n1 > n2:
                    increasing_number = False
                    break

            if increasing_number:
                result = max(result, num[i] * num[j])

    print(f"#{test_case} {result}")
