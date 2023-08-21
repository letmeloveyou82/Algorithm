N = int(input())
checkpoint = [list(map(int, input().split())) for _ in range(N)]

min_distance = int(1e9)
distance = 0
for i in range(N-1):
    distance += abs(checkpoint[i][0]-checkpoint[i+1][0]) + abs(checkpoint[i][1]-checkpoint[i+1][1])

for i in range(1, N-1):
    check_distance = distance
    check_distance -= abs(checkpoint[i][0]-checkpoint[i-1][0]) + abs(checkpoint[i][1]-checkpoint[i-1][1])
    check_distance -= abs(checkpoint[i+1][0]-checkpoint[i][0]) + abs(checkpoint[i+1][1]-checkpoint[i][1])
    check_distance += abs(checkpoint[i+1][0]-checkpoint[i-1][0]) + abs(checkpoint[i+1][1]-checkpoint[i-1][1])
    if min_distance > check_distance:
        min_distance = check_distance
print(min_distance)