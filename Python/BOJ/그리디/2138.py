N = int(input())
now_light = list(input())
hope_light = list(input())

def change(state):
    if state == '0':
        state = '1'
    else:
        state = '0'
    return state


def change_zero(light):
    cnt = 1
    light[0] = change(light[0])
    light[1] = change(light[1])
    for i in range(1, len(light)):
        if light[i-1] == hope_light[i-1]:
            continue
        else:
            cnt += 1
            light[i-1] = change(light[i-1])
            light[i] = change(light[i])
            if i < len(light)-1:
                light[i+1] = change(light[i+1])
    if hope_light == light:
        return cnt
    return int(1e9)


def non_change_zero(light):
    cnt = 0
    for i in range(1, len(light)):
        if light[i-1] == hope_light[i-1]:
            continue
        else:
            cnt += 1
            light[i-1] = change(light[i-1])
            light[i] = change(light[i])
            if i < len(light)-1:
                light[i+1] = change(light[i+1])
    if hope_light == light:
        return cnt
    return int(1e9)


cnt1 = change_zero(now_light[:])
cnt2 = non_change_zero(now_light[:])
ans = min(cnt1, cnt2)
if ans == int(1e9):
    ans = -1
print(ans)