n, m = map(int, input().split())
k = list(map(int, input().split()))

result = n*(n-1)//2 # n개 중 2개 골라 만들 수 있는 최대 조합 개수

for i in range(m):
    ball_count = k.count(i+1) # 각 무게에 해당하는 볼링공의 개수 카운트
    if ball_count >= 2: # 무게가 같은 볼링공의 개수가 2개 이상이면
        # 무게 같은 볼링공 중에서 2개 골랐을 때 만들 수 있는 조합을 구해 가장 최대로 나올 수 있는 조합에서 제외
        result -= ball_count*(ball_count-1)//2 

print(result)