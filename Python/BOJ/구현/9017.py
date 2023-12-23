import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    result_dict = defaultdict(list)
    data = list(map(int, input().split()))
    score = 1
    for i in range(N):
        team = data[i]
        if data.count(team) < 6:
            continue
        else:
            result_dict[team].append(score)
            score += 1
    min_score = int(1e9)
    winner = 0
    for team_num in result_dict.keys():
        if min_score > sum(result_dict[team_num][:4]):
            min_score = sum(result_dict[team_num][:4])
            winner = team_num
        elif min_score == sum(result_dict[team_num][:4]):
            if result_dict[winner][4] > result_dict[team_num][4]:
                winner = team_num
    print(winner)
