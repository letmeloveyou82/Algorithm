import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
A = []
for i in range(3):
    A.append(list(map(int, input().split())))

sec = 0
while sec <= 100:
    r_len = len(A)
    c_len = len(A[0])
    if r < r_len and c < c_len:
        if A[r][c] == k:
            print(sec)
            exit(0)
    if r_len > 100:
        A = [A[i] for i in range(100)]
    if c_len > 100:
        A = [A[i][0:100] for i in range(r_len)]

    if r_len >= c_len:
        # 모든 행에 대해서 정렬
        for i in range(r_len):
            tmp = []
            r_dict = Counter(A[i])
            for key in r_dict.keys():
                if key != 0:
                    tmp.append([key, r_dict[key]])
            tmp = sorted(tmp, key=lambda x:(x[1], x[0]))
            new_r = []
            for a, b in tmp:
                new_r.append(a)
                new_r.append(b)
            A[i] = new_r
        # max_r 기준으로 0 채운다.
        max_r = max(len(A[i]) for i in range(r_len))
        for i in range(r_len):
            while len(A[i]) < max_r:
                A[i].append(0)
    else:
        # 모든 열에 대해서 정렬
        after_c_list = []
        for j in range(c_len):
            column_list = []
            tmp = []
            for i in range(r_len):
                column_list.append(A[i][j])
            c_dict = Counter(column_list)
            for key in c_dict.keys():
                if key != 0:
                    tmp.append([key, c_dict[key]])
            tmp = sorted(tmp, key=lambda x:(x[1], x[0]))
            new_c = []
            for a, b in tmp:
                new_c.append(a)
                new_c.append(b)
            after_c_list.append(new_c)
        max_c = max(len(after_c_list[i]) for i in range(c_len))

        # max_c를 기준으로 0 채운다.
        for i in range(c_len):
            while len(after_c_list[i]) < max_c:
                after_c_list[i].append(0)
                
        # A 갱신
        A = [[0] * c_len for _ in range(max_c)]
        for i in range(max_c):
            for j in range(c_len):
                A[i][j] = after_c_list[j][i]
    sec += 1
print(-1)