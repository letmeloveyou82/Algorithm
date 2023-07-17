import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    mix_scoville = 0
    while True:
        if scoville[0] >= K:
            break
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        if len(scoville) == 0 and mix_scoville < K: # 모든 음식의 스코빌 점수를 K 이상으로 만들 수 없는 경우
            return -1
        answer += 1
        heapq.heappush(scoville, mix_scoville)
    return answer 