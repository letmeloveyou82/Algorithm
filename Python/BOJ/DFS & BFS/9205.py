from collections import deque
import sys

input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((home_x, home_y))
  while q:
    x, y = q.popleft()
    if abs(x - festival_x) + abs(y - festival_y) <= 1000:
      print('happy')
      return
    for i in range(n):
      if visited[i] == 0:
        new_x, new_y = graph[i]
        if abs(x - new_x) + abs(y - new_y) <= 1000:
          visited[i] = 1
          q.append((new_x, new_y))
  print('sad')
  return


for _ in range(int(input())):
  n = int(input())
  graph = []
  home_x, home_y = map(int, input().split())
  for _ in range(n):
    x, y = map(int, input().split())
    graph.append((x, y))
  festival_x, festival_y = map(int, input().split())
  visited = [0] * (n + 1)
  bfs()
