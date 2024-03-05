def solution(enroll, referral, seller, amount):
    result = []
    recommender = {} # 추천인
    profit = {} # 이익

    for i in range(len(enroll)):
        recommender[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
    
    for i in range(len(seller)):
        tmp = amount[i]*100
        parents = recommender[seller[i]]
        child = seller[i]
        
        while True:
            profit[child] += tmp - tmp//10
            tmp //= 10
            if parents == '-' or tmp == 0:
                break
            child = parents
            parents = recommender[child]
    
    for i in enroll:
        result.append(profit[i])

    return result