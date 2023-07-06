import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 전화번호의 수
    consistency = True
    number = sorted([input().rstrip() for _ in range(n)]) # 전화번호 목록 저장하고 오름차순 정렬
    for i in range(n-1):
        # 전화번호 목록에서 두 개씩 비교
        if number[i] == number[i+1][:len(number[i])]:
            consistency = False
            break
    if consistency == False:
        print("NO")
    else:
        print("YES")
