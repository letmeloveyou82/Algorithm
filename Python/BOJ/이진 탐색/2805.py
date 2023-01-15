# 이진 탐색으로 문제를 풀었을때 Python 3은 시간초과가 난다. PyPy3로 제출해야 한다.
# Counter 라이브러리를 사용하면 Python 3도 통과된다고 한다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

result = 0

# 이진 탐색을 위한 시작점과 끝점 생성
start = 0
end = max(tree)

# 이진 탐색 수행(반복적)
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in tree:
        if mid < i: # 잘랐을 때 가져갈 수 있는 나무 양 계산
            total += i - mid
    if total < m: # 나무 양이 부족한 경우, 더 많이 자르기(왼쪽 부분 탐색)
        end = mid - 1
    else: # 나무 양이 충분한 경우, 덜 자르기(오른쪽 부분 탐색)
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)