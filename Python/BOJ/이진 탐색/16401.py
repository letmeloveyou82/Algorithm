import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # 조카의 수, 과자의 수
snack_len = list(map(int, input().split()))
start = 1
end = max(snack_len)

result = 0
while start<=end:
    mid = (start + end) // 2
    count = 0 # 길이가 mid인 것을 만들 수 있는 개수
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
    if mid == 0:
        count = 0
        break
    for x in snack_len:
        if x >= mid:
            count += (x // mid)
    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)