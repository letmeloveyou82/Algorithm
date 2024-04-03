import sys

input = sys.stdin.readline
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

sum_dict = {0: 1} # 누적합을 저장할 딕셔너리

now_sum = 0
answer = 0

for i in numbers:
    now_sum += i

    # 현재까지 누적합 중에서 now_sum - (이전 누적합) = K가 있으면
    # 즉, 누적합 - K값이 이전에 나왔으면 정답 개수 추가
    if now_sum - K in sum_dict.keys():
        answer += sum_dict[now_sum - K]

    # 누적합 딕셔너리 갱신
    sum_dict[now_sum] = sum_dict.get(now_sum, 0) + 1

print(answer)
