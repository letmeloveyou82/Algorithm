from bisect import bisect_left
from itertools import product

def solution(dice):
    A = []
    n = len(dice)
    dice_num = [i for i in range(n)]
    result_dict = dict()
    
    # 주사위 굴리고 A가 이긴 횟수와 그때의 주사위 조합 result_dict에 저장
    def calculate_win(a, b):
        A_result = []
        B_result = []
        
        for i in product([d for d in range(6)], repeat = n//2):
            A_result.append(sum(dice[x][y] for x, y in zip(a, i)))
            B_result.append(sum(dice[x][y] for x, y in zip(b, i)))
        
        # 이분탐색
        B_result.sort()
        wins = sum(bisect_left(B_result, num) for num in A_result)
        result_dict[wins] = list(a)
    
    # A와 B가 주사위를 가져가는 조합
    def dfs(idx):
        if len(A) == n//2:
            B = []
            for i in range(n):
                if i not in A:
                    B.append(i)
            calculate_win(A, B)
            return
        for i in range(idx, n):
            A.append(dice_num[i])
            dfs(i+1)
            A.pop()
        
    dfs(0)
    max_key = max(result_dict.keys())

    return [x+1 for x in result_dict[max_key]]