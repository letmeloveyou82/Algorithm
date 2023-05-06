import sys
input = sys.stdin.readline

n = int(input()) # 상근이가 갖고 있는 숫자 카드 개수
sanggeun_card = sorted(list(map(int, input().split())))
m = int(input()) # 갖고 있는지 판단할 숫자 카드 개수
judgment_num = list(map(int, input().split()))
ans = []

# 이진 탐색
def binary_search(data, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid -1 
        else:
            start = mid + 1
    return None

for target in judgment_num:
    result = binary_search(sanggeun_card, target, 0, n-1)
    if result == None:
        ans.append("0")
    else:
        ans.append("1")
print(" ".join(ans))