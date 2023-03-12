from collections import deque

n = int(input())
dq = deque(enumerate(map(int, input().split()))) # enumerate를 사용해 인덱스 정보와 값을 함께 저장

result = []

while dq:
    idx, move = dq.popleft() # 터트리는 풍선의 idx, 풍선 안에 있는 종이의 값
    result.append(idx+1) 
    if move > 0: # 양수 (오른쪽 이동)
        dq.rotate(-(move-1)) # 이미 pop할 때 왼쪽으로 1번 이동했으니까 -1 해줌
    else: # 음수 (왼쪽 이동)
        dq.rotate(-move) # 참고로 deque rotate 메소드는 +1이 왼쪽으로 1칸 이동이라 - 부호 붙여줌

for i in result:
    print(i, end = ' ')