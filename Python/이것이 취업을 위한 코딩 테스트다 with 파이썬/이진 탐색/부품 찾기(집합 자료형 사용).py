# 방법 3) 집합 자료형 (가장 간결한 코드)
import sys

input = sys.stdin.readline
n = int(input())

# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
# set을 활용할 경우 무조건 O(1), 즉 상수 시간으로 유무 검사를 해준다.
data = set(map(int, input().split())) 

m = int(input())
find_data = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in find_data:
    # 해당 부품이 존재하는지 확인
    if i in data:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')