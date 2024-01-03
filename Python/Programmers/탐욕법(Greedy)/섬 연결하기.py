def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    link = set([costs[0][0]])
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(link) != n: # set 안에 연결된 모든 위치가 연결되기 전까지 실행
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link: # 두 섬 중 하나가 연결이 되어있지 않을 때 비용 더하기
                link.update([v[0], v[1]]) # 이미 섬이 연결되었을 경우 중복된 섬은 추가되지 않고 최대 n개의 섬을 유지
                answer += v[2]
                break
                
    return answer