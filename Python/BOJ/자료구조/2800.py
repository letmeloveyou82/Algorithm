from itertools import combinations
import sys
input = sys.stdin.readline

answer = set() # 서로 다른 식을 출력해야 하기 때문에 중복 제거를 위해 set 사용
stack = []
temp = []
expression = list(input().rstrip()) # 오른쪽 \n 제거를 위해 rstrip 사용

# 반복문을 통해 괄호의 시작점과 끝점 idx 저장
for idx, v in enumerate(expression):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        temp.append([start, end])

for i in range(1, len(temp) + 1): # 조합은 1개 이상 선택하는 거니까 1에서 시작
    c = combinations(temp, i) # combinations를 통해 모든 경우의 수를 확인
    # 반복문을 통해 경우의 수를 확인
    for j in c:
        target = list(expression)

        # 괄호 제거
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""
        
        answer.add(''.join(target)) # 괄호 제거한 식을 answer에 저장

for ans in sorted(list(answer)): # 사전 순이라 sorted
    print(ans)