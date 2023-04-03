import sys
input = sys.stdin.readline
n = int(input()) # 수열의 크기
num_list = list(map(int, input().split()))
x = int(input()) # 구하고자 하는 두 수의 합
num_list.sort() # 오름차순 정렬
count = 0 
interval_sum = 0
left = 0
right = n-1

# 투 포인터
while left < right:
    interval_sum = num_list[left] + num_list[right]
    if interval_sum == x: 
        count += 1
    if interval_sum < x:
        left += 1
        continue
    right -= 1
print(count)
