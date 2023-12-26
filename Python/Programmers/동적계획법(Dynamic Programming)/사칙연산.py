def solution(arr):
    nums = []
    op = []
    for i in arr:
        if i != '+' and i!='-':
            nums.append(int(i))
        else:
            op.append(i)
    N = len(nums) # 피연산자 개수
    dp_min = [[float('inf')] * N for _ in range(N)] # 최솟값 DP
    dp_max = [[float('-inf')] * N for _ in range(N)] # 최댓값 DP
    for length in range(N):
        for start in range(N-length):
            end = start+length
            if start == end: # 해당 구간에 숫자가 한 개만 있는 경우 그 숫자가 해당 구간의 최댓값이자 최솟값이 됨
                dp_min[start][end] = dp_max[start][end] = nums[start]
                continue
            for mid in range(start, end): # 중간 지점 mid를 기준으로 왼쪽과 오른쪽으로 나누어, 각각의 경우에 대해 최댓값과 최솟값을 갱신
                if op[mid] == '+':
                    dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid+1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid+1][end], dp_min[start][end])
                elif op[mid] == '-':
                    dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid+1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid+1][end], dp_min[start][end])

    return dp_max[0][-1]