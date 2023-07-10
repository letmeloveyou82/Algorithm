def solution(genres, plays):
    answer = []
    genres_count = dict() # 장르별 재생수 count할 dict
    genres_and_plays = dict() # 장르를 key로, [재생수, 고유번호]를 value로 저장할 dict

    for i in range(len(genres)):
        if genres_and_plays.get(genres[i]) == None:
            genres_and_plays[genres[i]] = [[plays[i], i]]
            genres_count[genres[i]] = plays[i]
        else:
            genres_and_plays[genres[i]].append([plays[i], i])
            genres_count[genres[i]] += plays[i]
		
	# 1. 가장 많이 재생된 장르 순서
    genres_count_desc = sorted(genres_count, reverse=True, key=lambda x: genres_count[x])

    # 2. 장르별 재생 많은 순서, 3. 재생 값 같다면 고유번호 적은 순서
    for key in genres_and_plays:
        genres_and_plays[key].sort(key=lambda x:(-x[0], x[1]))

    for g in genres_count_desc:
        if len(genres_and_plays[g]) == 1: # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
            answer.append(genres_and_plays[g][0][1])
        elif len(genres_and_plays[g]) >= 2:
            answer.append(genres_and_plays[g][0][1])
            answer.append(genres_and_plays[g][1][1])
    return answer