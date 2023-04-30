import sys
input = sys.stdin.readline
n = int(input()) # 사진틀의 개수
total_recommend = int(input()) # 전체 학생의 총 추천 횟수
candidate = list(map(int, input().split()))
photo_frame = dict()

for i in range(total_recommend):
    if candidate[i] in photo_frame:
        photo_frame[candidate[i]][0] += 1
    else:
        if len(photo_frame) < n:
            photo_frame[candidate[i]] = [1, i] # [추천수, 오래된 순]
        else:
            del_list = sorted(photo_frame.items(), key = lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo_frame[del_key])
            photo_frame[candidate[i]] = [1, i]

answer_list = list(sorted(photo_frame.keys()))
print(*answer_list)