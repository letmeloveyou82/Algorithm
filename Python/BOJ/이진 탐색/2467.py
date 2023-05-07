import sys

input = sys.stdin.readline
n = int(input()) # 전체 용액의 수
solution = list(map(int, input().split()))
ans = float("INF")
ans_left = 0 # 출력하고자 하는 용액 중 첫 번째 용액의 idx
ans_right = 0 # 출력하고자 하는 용액 중 두 번쨰 용액의 idx

for i in range(n-1):
    current = solution[i]

    start = i + 1
    end = n-1
    while start <= end:
        mid = (start+end)//2
        tmp = current + solution[mid]
        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid
            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(solution[ans_left], solution[ans_right])