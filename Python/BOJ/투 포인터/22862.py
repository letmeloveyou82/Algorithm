import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = list(map(int, input().split()))

max_length = 0 # 짝수로 이뤄져 있는 연속한 부분 수열 중 가장 긴 길이
end = 0 # 끝 포인터 
tmp_length = 0 # 현재 짝수 부분 수열의 길이
odd = 0 # 지우려는 홀수 카운트

# start를 N까지 계속 증가시키며 반복 
for start in range(N):
    while odd <= K and end < N:# end를 가능한 만큼 이동
        if S[end] % 2 == 1: # 홀수
            odd += 1
        else: # 짝수 
            tmp_length += 1
        end += 1 # 끝 점 이동

        if start == 0 and end == N:
            max_length = tmp_length
            break
            
    if odd == K+1:
        max_length = max(tmp_length, max_length)
    
    if S[start] % 2 == 1: # 시작점이 홀수
        odd -= 1
    else: # 시작점이 짝수
        tmp_length -= 1
print(max_length)
