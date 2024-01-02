N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
    exit(0)

ranking_list = list(map(int, input().split()))
higher_score = 0
same_score = 0

for i in range(N):
    if new_score < ranking_list[i]:
        higher_score += 1
    elif new_score == ranking_list[i]:
        same_score += 1

if higher_score + same_score >= P:
    print(-1)
else:
    print(higher_score+1)