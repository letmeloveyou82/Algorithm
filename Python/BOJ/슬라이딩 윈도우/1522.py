s = input()
a = s.count('a') # 입력된 문자열에서의 a의 개수

s += s[0:a-1] # 원형 문자열 처리(0 ~ a의 개수-1만큼의 값을 주어진 문자열 뒤에 붙여줌)
min_val = float('inf') # 최솟값
for i in range(len(s)-(a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)