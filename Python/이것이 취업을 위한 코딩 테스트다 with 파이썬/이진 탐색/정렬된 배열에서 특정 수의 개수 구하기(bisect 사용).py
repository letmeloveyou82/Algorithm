# 방법 1) 파이썬의 이진 탐색 라이브러리 bisect 활용 (나의 풀이)
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

if count == 0: # 값이 x인 원소가 존재하지 않는다면
    print(-1)
else: # 값이 x인 원소가 존재한다면
    print(count)
