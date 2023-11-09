def dfs(n):
    global ans 
    if n == change_num:
        ans = max(ans, int("".join(map(str, numbers))))
        return
    
    # N개에서 2개 뽑는 모든 조합 (둘을 교환)
    for i in range(N-1):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            check_key = int("".join(map(str, numbers)))
            if (n, check_key) not in visited:
                dfs(n+1)
                visited.append((n, check_key))

            numbers[i], numbers[j] = numbers[j], numbers[i] # 원상복구
            
T = int(input())
for test_case in range(1, T+1):
    temp, c = input().split()
    change_num = int(c)
    numbers = list(map(int, temp))
    N = len(numbers)
    ans = 0
    visited = []
    dfs(0)
    print(f"#{test_case} {ans}")