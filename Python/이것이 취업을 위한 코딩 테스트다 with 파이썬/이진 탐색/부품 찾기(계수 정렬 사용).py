# 방법 2) 계수 정렬 
import sys

input = sys.stdin.readline
n = int(input()) # 가게의 부품 개수 입력
data = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    data[int(i)] = 1

m = int(input()) # 손님이 확인 요청한 부품 개수 입력
find_data = list(map(int, input().split())) # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in find_data:
    if data[i] == 1:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')