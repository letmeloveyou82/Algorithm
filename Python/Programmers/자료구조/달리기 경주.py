from collections import defaultdict

def solution(players, callings):
    ranking_dict = defaultdict(int)
    for i in range(len(players)):
        ranking_dict[players[i]] = i

    for name in callings:
        idx = ranking_dict[name]
        front_player = players[idx-1]
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        ranking_dict[name] -= 1
        ranking_dict[front_player] += 1
        
    return players