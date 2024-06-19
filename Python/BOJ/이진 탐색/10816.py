import sys
input = sys.stdin.readline

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
answer = []

def left_index(target):
    start, end = 0, N
    while start < end:
        mid = (start+end)//2
        if card[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

def right_index(target):
    start, end = 0, N
    while start < end:
        mid = (start+end)//2
        if card[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end

for i in range(M):
    answer.append(right_index(check[i]) - left_index(check[i]))

print(*answer)