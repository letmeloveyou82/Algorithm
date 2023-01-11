'''
이진 탐색을 이용해 해결할 수 있는 파라메트릭 서치 유형 문제
C보다 많은 개수로 공유기를 설치할 수 있다면 '가장 인접한 두 공유기 사이의 거리'의 값을 증가시켜서,
더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색 수행
'''
import sys 
input = sys.stdin.readline

n, c = map(int, input().split()) # 집의 개수 n과 공유기의 개수 c개 입력
coordinates = [] # 집의 좌표을 담을 리스트
for _ in range(n): # 집의 좌표를 리스트에 저장
    coordinates.append(int(input()))
coordinates.sort() # 집의 좌표 오름차순 정렬

start = 1 # 가능한 최소 거리(min gap)
end = coordinates[-1] - coordinates[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = coordinates[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if coordinates[i] >= value + mid:
            value = coordinates[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1 

print(result)