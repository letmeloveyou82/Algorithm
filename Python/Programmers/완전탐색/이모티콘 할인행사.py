from itertools import product

def solution(users, emoticons):
    answer = []
    discount_perc = [10, 20, 30, 40] # 이모티콘 할인율
    
    for case in product(discount_perc, repeat=len(emoticons)):
        result = [0, 0]
        for user in users: 
            tmp = 0 # user의 이모티콘 구입 지불 비용
            for idx, sale in enumerate(case):
                if sale >= user[0]: 
                    tmp += emoticons[idx] * (100 - sale) // 100
            if tmp >= user[1]: 
                result[0] += 1
            else: 
                result[1] += tmp
        answer.append(result)
    # 이모티콘 플러스 가입자 최대(우선순위), 이모티콘 판매액 최대로 정렬
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]