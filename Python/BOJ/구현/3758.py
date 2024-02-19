import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split()) # 팀 개수, 문제 개수, 나의 팀 ID, 로그 엔트리 개수
    score_board = [[team_num, dict(), 0, 0] for team_num in range(n+1)] # 팀 ID, 문제 번호별 획득점수 저장할 dict, 제출횟수, 제출시간 

    for num in range(m):
        i, j, s = map(int, input().split()) # 팀 ID, 문제 번호, 획득 점수

        if score_board[i][1].get(j) == None:
            score_board[i][1][j] = s
        else:
            if score_board[i][1][j] < s:
                score_board[i][1][j] = s
        score_board[i][2] += 1
        score_board[i][3] = num

    score_board.sort(key=lambda x: (-sum(x[1].values()), x[2], x[3]))

    ranking = 1
    for i in range(n):
        if score_board[i][0] != t:
            ranking += 1
        else:
            break

    print(ranking)