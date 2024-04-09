import sys
input = sys.stdin.readline
n = int(input())
a = [input().rstrip() for _ in range(n)]

# 입력받은 문자들을 인덱스와 함께 사전순으로 정렬
b = sorted(list(enumerate(a)), key=lambda x: x[1])

# 두 단어를 앞에서부터 비교해 나올 수 있는 최장 접두사 길이 리턴하는 함수
def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt

# 들어온 순서대로 단어의 최장 접두사 길이 저장해둘 리스트 0으로 초기화
length = [0] * (n + 1)
max_length = 0

for i in range(n - 1):
    # 인접한 두 단어를 check 함수에 대입
    tmp = check(b[i][1], b[i + 1][1])
    # 최장 접두사 길이 갱신
    max_length = max(max_length, tmp)
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i + 1][0]] = max(length[b[i + 1][0]], tmp)

first = 0
for i in range(n):
    # 입력된 순서대로 접두사의 길이 비교
    if first == 0:
        # 만약 현재 접두사의 길이가 최장 접두사라면
        if length[i] == max(length):
            # 제일 먼저 입력된 문자 출력
            first = a[i]
            print(first)
            pre = a[i][:max_length]
    else:
        # 다음으로 입력되었된 값들 중 최장 접두사 출력 후 종료
        if length[i] == max(length) and a[i][:max_length] == pre:
            print(a[i])
            break