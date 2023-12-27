def solution(distance, rocks, n):
    answer = 0
    start = 1 
    end = distance 
		
    rocks.sort()
    rocks.append(distance) # 도착지점 추가

    while start <= end:
        mid = (start+end)//2
        del_rock_cnt = 0 # 제거한 바위 개수
        pre_rock = 0 # 기준이 되는 바위(시작지점) 위치
        for rock in rocks:
            if rock - pre_rock < mid: # 바위 사이의 거리가 가정한 값보다 작으면 제거
                del_rock_cnt += 1
            else: # 아니라면 그 바위를 새로운 기준으로 세움
                pre_rock = rock
            if del_rock_cnt > n: # 제거된 돌이 문제 조건보다 많으면 break
                break

        if del_rock_cnt > n: # 초과 제거한 경우 
            end = mid - 1
        else: # 이하 제거한 경우 
            answer = mid
            start = mid + 1
            
    return answer