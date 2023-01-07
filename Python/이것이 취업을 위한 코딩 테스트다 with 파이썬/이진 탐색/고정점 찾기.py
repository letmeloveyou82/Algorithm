import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

# 이진 탐색 소스코드 구현(반복문 사용)
def find_fixed_point(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid: # 고정점을 찾은 경우 인덱스 반환
            return mid
        elif mid > array[mid]: # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
            start = mid + 1
        else: # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
            end = mid - 1
    return None

# 이진 탐색(Binary Search) 수행
fixed_point = find_fixed_point(array, 0, n-1)

if fixed_point == None: # 고정점이 없는 경우 -1 출력
    print(-1)
else: # 고정점이 있는 경우 해당 인덱스 출력
    print(fixed_point)