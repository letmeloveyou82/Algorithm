def solution(edges):
    answer = [0, 0, 0, 0]
    edge_cnt = dict()
    for a, b in edges:
        if not edge_cnt.get(a):
            edge_cnt[a] = [0, 0] # [나가는 간선 수, 들어오는 간선 수]
        if not edge_cnt.get(b):
            edge_cnt[b] = [0, 0] 
            
        edge_cnt[a][0] += 1
        edge_cnt[b][1] += 1
        
    for key, cnt in edge_cnt.items():
        if cnt[0] >= 2 and cnt[1] == 0:
            answer[0] = key
        elif cnt[0] == 0 and cnt[1] > 0:
            answer[2] += 1
        elif cnt[0] >= 2 and cnt[1] >= 2:
            answer[3] += 1
    answer[1] = edge_cnt[answer[0]][0] - answer[2] - answer[3]
    
    return answer