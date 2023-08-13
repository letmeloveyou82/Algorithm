from collections import deque
N = int(input())
card = deque([i for i in range(1, N+1)])
while True:
    if len(card) == 1:
        break
    card.popleft()
    card.rotate(-1)
print(card[0])