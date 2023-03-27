import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 책의 개수 n, 한 번에 들 수 있는 책의 개수 m
plus_location = [] # 양수 리스트
minus_location = [] # 음수 리스트
distance = [] # 걸음 수에 영향을 주는 거리
for i in list(map(int, input().split())):
    if i < 0:
        minus_location.append(abs(i))
    else:
        plus_location.append(i)

# 왼쪽 방향으로 책 가져다 놓을 때
minus_location.sort(reverse=True)
for i in range(len(minus_location)//m): # 한 번에 m개씩 가져갈 수 있기 때문에 m으로 나눈 몫만큼 반복
    distance.append(minus_location[m*i])
if len(minus_location) % m > 0: # m개씩 가져다 놓을 수 있을 만큼 가져다 놓고도 남은 것 중 가장 큰 값 distance에 추가
    distance.append(minus_location[(len(minus_location)//m)*m])

# 오른쪽 방향으로 책 가져다 놓을 때
plus_location.sort(reverse=True)
for i in range(len(plus_location)//m):
    distance.append(plus_location[m*i])
if len(plus_location) % m > 0:
    distance.append(plus_location[(len(plus_location)//m)*m])

distance.sort() # 걸음 수에 영향을 주는 거리들 오름차순 정렬
result = distance.pop() # 가장 멀리 있는 책의 위치는 마지막에 갖다 놓으러 감 (0 위치로 안 와도 되니까)
result += 2*sum(distance) # 갔다가 다시 0으로 돌아오기 때문에 거리 2배하고 더해줌
print(result)