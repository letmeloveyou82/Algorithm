def dfs(index, sum_score, sum_kcal):
    global max_score

    # Limit 보다 크면 탐색 종료
    if sum_kcal > L:
        return

    # 기존에 저장된 최대 점수보다 크면 갱신
    if max_score < sum_score:
        max_score = sum_score

    # 마지막 재료까지 다 확인하면 탐색 종료
    if index == N:
        return

    score, kcal = ingredients[index]

    dfs(index+1, sum_score + score, sum_kcal + kcal) # 재료 사용했을 때
    dfs(index+1, sum_score, sum_kcal) # 재료 사용 안 했을 때

T = int(input())
for test_case in range(1, T+1):
    result = []
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {max_score}")