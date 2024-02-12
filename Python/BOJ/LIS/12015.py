import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def lis_with_binary_search():
    dp = [float('inf')] * (N + 1)
    dp[0] = float('-inf')
    lis_length = 0

    for num in arr:
        # 이분 탐색 수행
        left, right = 0, lis_length
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        # dp 리스트 업데이트
        dp[left] = num
        if left > lis_length:
            lis_length = left

    return lis_length

print(lis_with_binary_search())