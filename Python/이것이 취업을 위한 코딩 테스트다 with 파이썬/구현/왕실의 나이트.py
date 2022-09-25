now = input()
row = int(now[1])
# ord('문자') : 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
column = int(ord(now[0]))-int(ord('a')) + 1

available = [(2, -1),(-2, 1), (2, 1), (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
result = 0
for i in available:
    next_row = row + i[1]
    next_column = column + i[0]
    if next_row>=1 and next_column>=1 and next_row<=8 and next_column<=8:
        result +=1 
print(result)