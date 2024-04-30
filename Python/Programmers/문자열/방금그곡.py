def solution(m, musicinfos):
    answer = []
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L').replace('B#', 'M')

    for now in range(len(musicinfos)):
        s, e, title, melody = musicinfos[now].split(',')
        sh, sm = s.split(':')
        eh, em = e.split(':')
        melody = melody.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L').replace('B#', 'M')
        melody_play_time = int(eh)*60+int(em) - ((int(sh)*60)+int(sm))
        if len(melody) < melody_play_time:
            tmp = ''
            for i in range(melody_play_time-len(melody)):
                tmp += melody[i%len(melody)]
            melody += tmp
        else:
            melody = melody[:melody_play_time]
        if m in melody:
            answer.append([melody_play_time, now, title])
            
    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x : (-x[0], x[1]))
        return answer[0][2]