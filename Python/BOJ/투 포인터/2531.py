from collections import defaultdict
n, d, k, c = map(int, input().split()) # 접시 수, 초밥가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
plate = []
for i in range(n):
    plate.append(int(input()))
left, right = 0, 0
dict = defaultdict(int)
result = 0

# k 만큼 먹기
while right < k:
    dict[plate[right]] += 1
    right += 1

# c는 반드시 추가
dict[c] += 1

# 슬라이딩 윈도우
while left < n:
    result = max(result, len(dict))
    # 맨 왼쪽 초밥 제거
    dict[plate[left]] -= 1
    # 삭제된 왼쪽 초밥이 0이면 dict 삭제
    if dict[plate[left]] == 0:
        del dict[plate[left]]
    dict[plate[right%n]] += 1
    left += 1
    right += 1

print(result)