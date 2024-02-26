import sys
input = sys.stdin.readline

N, M = map(int, input().split())
daily_usage = [int(input()) for _ in range(N)]

left = min(daily_usage)
right = sum(daily_usage)

while left <= right:
    mid = (left+right)//2
    wallet = mid # 현재 가진 돈
    withdraw = 1 # 인출 횟수
    for i in range(N): 
        if wallet < daily_usage[i]: # 가진 돈이 부족하면 돈 인출
            wallet = mid
            withdraw += 1
        wallet -= daily_usage[i]

		# M번보다 많이 인출하거나 인출 금액이 하루 다 살기에 적은 경우 (인출 금액이 적음)
    if withdraw > M or mid < max(daily_usage):
        left = mid + 1
    else: # 인출 횟수가 M번보다 적거나 같은 경우 (인출 금액이 많음)
        right = mid - 1
        K = mid # K값 저장

print(K)