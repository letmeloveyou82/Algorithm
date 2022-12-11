n = int(input())

# N명의 학생 정보 입력받아 (이름, 점수) 튜플 형태로 묶고, 리스트에 저장 
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
# lambda 매개변수 : 표현식
array = sorted(array, key=lambda student:student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')