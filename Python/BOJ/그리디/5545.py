import sys 
input = sys.stdin.readline
n = int(input()) # 토핑 종류의 수 n
a, b = map(int, input().split()) # 도우의 가격 a , 토핑의 가격 b
c = int(input()) # 도우의 열량 c
topping = [] # 토핑의 열량 리스트
for _ in range(n):
    topping.append(int(input()))
topping.sort(reverse=True) # 내림차순 정렬

result = c / a # 토핑을 0개 선택했을 경우
for i in range(1, len(topping)+1): # 토핑을 1개 이상 선택했을 경우
    calory = c + sum(topping[0:i]) # 피자의 열량
    price = a + (b*i) # 피자의 가격
    if calory / price > result: # max인지 판단
        result = calory / price
    else:
        break
        
print(int(result))