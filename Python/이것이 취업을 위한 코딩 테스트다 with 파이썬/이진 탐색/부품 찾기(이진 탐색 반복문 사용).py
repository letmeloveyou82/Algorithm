# 방법 1) 이진 탐색 구현 (반복문 사용)
import sys

input = sys.stdin.readline
n = int(input()) # 가게 부품 개수 입력
data = list(map(int, input().split())) # 가게에 있는 전체 부품 번호를 공백으로 구분해 입력
data.sort() # 이진 탐색 수행하기 위해 사전에 정렬 수행
m = int(input()) # 손님이 확인 요청한 부품 개수 입력
find_data = list(map(int, input().split())) # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분해 입력

def binary_search(data, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 손님이 확인 요청한 부품 번호 하나씩 확인
for target in find_data:
    result = binary_search(data, target, 0, n-1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')