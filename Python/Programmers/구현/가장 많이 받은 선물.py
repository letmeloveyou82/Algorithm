def solution(friends, gifts):
    n = len(friends)
    answer = [0] * n
    idx_dict = dict()
    for i in range(n):
        idx_dict[friends[i]] = i
    
    give_and_take = [[0 for _ in range(n)] for _ in range(n)]
    for g in gifts:
        a, b = g.split()
        give_and_take[idx_dict[a]][idx_dict[b]] += 1

    gf_point = [0] * n
    for i in range(n):
        g_cnt = sum(give_and_take[i])
        t_cnt = sum(give_and_take[j][i] for j in range(n))
        gf_point[i] = g_cnt-t_cnt

    for i in range(n):
        for j in range(n):
            if i != j and give_and_take[i][j] != -1 and give_and_take[j][i] != -1:
                if (give_and_take[i][j] == 0 and give_and_take[j][i] == 0) or give_and_take[i][j] == give_and_take[j][i]:
                    if gf_point[i] < gf_point[j]:
                        answer[j] += 1
                    elif gf_point[i] > gf_point[j]:
                        answer[i] += 1
                elif give_and_take[i][j] < give_and_take[j][i]:
                    answer[j] += 1
                elif give_and_take[i][j] > give_and_take[j][i]:
                    answer[i] += 1
                give_and_take[i][j] = -1
                give_and_take[j][i] = -1
                    
    return max(answer)