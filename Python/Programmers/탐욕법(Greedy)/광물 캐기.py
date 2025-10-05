def solution(picks, minerals):
    answer = 0
    # 곡괭이 수 구함
    gokgaeong_cnt = sum(picks)
    
    # 곡괭이로 캘 수 있는 광물만큼 자름
    num = gokgaeong_cnt * 5
    if len(minerals) > gokgaeong_cnt:
        minerals = minerals[:num]
    
    # 광물 조사
    new_minerals = [[0, 0, 0] for _ in range((len(minerals) // 5 + 1))]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond' :
            new_minerals[i//5][0] += 1
        elif minerals[i] == 'iron' :
            new_minerals[i//5][1] += 1
        elif minerals[i] == 'stone' :
            new_minerals[i//5][2] += 1
    # 광물 순서를 다이아몬드, 철, 돌 많은 순으로 정렬함
    new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    for i in new_minerals:
        dia, iron, stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia+iron+stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5*dia)+iron+stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25*dia)+(5*iron)+stone
                break
    return answer