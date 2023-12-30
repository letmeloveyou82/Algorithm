N, K = map(int, input().split())
data = list(input())
visited = [0] * N
result = 0

for i in range(N):
    if data[i] == 'P':
        for j in range(i - K, i + K + 1):
            if 0 <= j < N and data[j] == 'H' and visited[j] == 0:
                visited[j] = 1
                result += 1
                break
print(result)