def solution(video_len, pos, op_start, op_end, commands):
    # "mm:ss" 형태 몇 초인지 return
    def second(str):
        min, sec = map(int, str.split(":"))
        return min*60+sec
    
    answer = ''
    now = second(pos)
    video_end = second(video_len)
    op_start = second(op_start)
    op_end = second(op_end)

    for c in commands:
        if op_start <= now <= op_end:
            now = op_end
        if c == "next":
            if video_end - now < 10 : now = video_end
            else: now += 10
        elif c == "prev":
            if now < 10 : now = 0
            else: now -= 10
        if op_start <= now <= op_end:
            now = op_end

    a, b = divmod(now, 60)
    if a < 10: 
        answer += "0"+str(a)
    else:
        answer += str(a)
    answer += ":"
    if b < 10: 
        answer += "0"+str(b)
    else:
        answer += str(b)
    return answer