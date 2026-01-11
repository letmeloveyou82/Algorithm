import sys

input = sys.stdin.readline

# 현재 휴게소 개수, 더 지으려고 하는 휴게소 개수, 고속도로 길이
N, M, L = map(int, input().split())

# N이 0일 수도 있음
if N > 0:
    rest = list(map(int, input().split()))
else:
    rest = []

rest.append(0)
rest.append(L)
rest.sort()

def can(mid: int) -> bool:
    need = 0
    for i in range(len(rest)-1):
        diff = rest[i+1] - rest[i]
        need += (diff - 1) // mid
        if need > M :
            return False
    return True

low, high = 1, L
answer = L
while low <= high:
    mid = (low + high) // 2
    if can(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)