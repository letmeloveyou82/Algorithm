import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 개수

for i in range(t):
    n = int(input()) # 통나무의 개수
    log_height = list(map(int, input().split())) # 각 통나무의 높이 리스트
    log_height.sort() # 오름차순 정렬
    difficulty = 0 # 난이도 
    for j in range(2, n):
        difficulty = max(difficulty, abs(log_height[j]-log_height[j-2]))
    print(difficulty)
