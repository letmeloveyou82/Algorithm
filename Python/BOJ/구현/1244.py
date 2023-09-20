# 스위치 상태 바꾸는 함수
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

switch_num = int(input())
switch = [-1] + list(map(int, input().split()))

# 남 1 여 2로 표시
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, switch_num+1, num):
            change(i)
    else:
        change(num)
        # 좌우대칭 확인
        for i in range(switch_num//2):
            if num-i < 1 or num+i > switch_num:
                break
            if switch[num-i] == switch[num+i]:
                change(num-i)
                change(num+i)
            else:
                break

# 20개씩 출력
for i in range(1, switch_num+1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()