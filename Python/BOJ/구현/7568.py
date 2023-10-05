n = int(input())
body = [tuple(map(int, input().split())) for _ in range(n)] # (몸무게, 키)
rank = [1] * n

for i in range(n):
  weight, height = body[i]
  for j in range(n):
    if i != j and weight < body[j][0] and height < body[j][1]:
      rank[i] += 1
      
print(*rank)