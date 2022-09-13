# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
array = list(map(int, input().split()))

array.sort() # 입력받은 수들 정렬하기

sum = array[-1] * M # 가장 큰 수를 M번 더하기
diff = array[-1] - array[-2] # 가장 큰 수와 두 번째로 큰 수의 차이
count = M // (K+1) # 두 번째로 큰 수가 와야 하는 자리의 수 계산
sum = sum - (diff*count)
print(sum) # 최종 답안 출력