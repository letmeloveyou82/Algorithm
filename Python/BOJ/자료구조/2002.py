import sys
input = sys.stdin.readline

n = int(input()) # 차의 대수
enter_car = [input().rstrip() for _ in range(n)] # 터널 입장한 차량 번호
count = 0

for _ in range(n):
    num = input().rstrip()
    if enter_car[0] != num:
        count += 1
    enter_car.remove(num)
    
print(count)