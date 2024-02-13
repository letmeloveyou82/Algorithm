from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
time = 0
bridge = deque([0] * w)

while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(time)