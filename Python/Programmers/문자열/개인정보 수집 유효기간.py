def solution(today, terms, privacies):
    def change_day(str):
        Y, M, D = map(int, str.split("."))
        return Y*12*28+M*28+D
    
    answer = []
    terms_dict = dict()
    for t in terms:
        k, m = t.split()
        terms_dict[k] = int(m)*28
    
    today = change_day(today)
    for i in range(len(privacies)):
        date, k = privacies[i].split()
        if today >= change_day(date) + terms_dict[k]:
            answer.append(i+1)
        
    return answer