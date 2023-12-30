p, m = map(int, input().split()) # 플레이어 수, 방의 정원
room = []
for _ in range(p):
    now = input().split()
    go_in = False
    if len(room) == 0:
        room.append([[int(now[0]), now[1]]])
        go_in = True
    else:
        for i in range(len(room)):
            if len(room[i]) == m:
                continue
            if room[i][0][0] - 10 <= int(now[0]) <= room[i][0][0] + 10:
                room[i].append([int(now[0]), now[1]])
                go_in = True
                break
    if not go_in:
        room.append([[int(now[0]), now[1]]])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    people = sorted(room[i], key=lambda x: x[1])
    for p in people:
        print(*p)