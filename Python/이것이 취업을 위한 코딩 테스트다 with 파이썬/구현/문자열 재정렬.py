# ----------------------- 내가 짠 코드 -----------------------
# s = list(input())

# s.sort()
# sum = 0
# idx = 0
# for i in s:
#     if ord(i) < 65:
#         sum += int(i)
#         idx += 1
#     else:
#         break
# temp = ""
# for k in range(idx, len(s)):
#     temp += s[k]
# print(temp+str(sum))

# ----------------------- 답안 예시 코드 -----------------------
s = input()
result = []
sum = 0

# 문자 하나씩 확인
for i in s:
    # 알파벳인 경우 결과 리스트에 삽입
    # 문자열.isalpha() : 문자열의 구성이 알파벳인지 확인하는 함수 (문자열에 숫자 및 공백 있으면 False 리턴)
    if i.isalpha():
        result.append(i)
    # 숫자는 따로 더하기
    else:
        sum += int(i)

# 알파벳 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if sum != 0:
    result.append(str(sum))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# '구분자'.join(리스트명) : 리스트를 문자열로 변환하는 함수 
print(''.join(result))