# 퀵 정렬 -> 시간 초과, 메모리 초과 : 평균적으로는 O(NlogN)인데 최악의 경우 O(N^2) 라서 그런 것 같음
# 파이썬 정렬 라이브러리(O(NlogN)) -> 성공
import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
for i in sorted(array):
    print(i)