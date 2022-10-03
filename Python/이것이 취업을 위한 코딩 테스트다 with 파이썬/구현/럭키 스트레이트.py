n = int(input())
list = str(n)
length = len(list) # 점수값의 총 자리수
slice_position = length // 2

left = 0
right = 0
# 왼쪽 부분의 자릿수 합 더하기
for i in range(slice_position):
    left += int(list[i])

# 오른쪽 부분의 자릿수 합 더하기
for j in range(slice_position, length):
    right += int(list[j])
    
if(right == left):
    print("LUCKY")
else:
    print("READY")