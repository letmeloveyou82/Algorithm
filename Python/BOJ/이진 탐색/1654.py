K, N = map(int, input().split())
LAN_length = [int(input()) for _ in range(K)]

left = 1
right = sum(LAN_length) // N

while left <= right:
    mid = (left+right)//2
    LAN_cnt = 0
    for i in LAN_length:
        LAN_cnt += i//mid
    if LAN_cnt >= N:
        left = mid+1
    else:
        right = mid-1

print(left-1)