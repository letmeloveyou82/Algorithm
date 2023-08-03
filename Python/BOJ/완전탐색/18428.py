import sys
input = sys.stdin.readline

n = int(input())
graph = []
teacher = 0
for _ in range(n):
  line = list(input().split())
  teacher += line.count('T')
  graph.append(line)

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

# T의 위치에서 상,하,좌,우 일직선으로 학생이 있는지 확인하는 함수
def check_S(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 상하좌우로 확인
    while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
      if graph[nx][ny] == 'S':
        # 감시 가능
        return True            
      else:        
        # T나 X면 계속 탐색
        nx += dx[i]
        ny += dy[i]
  # 감시 불가능
  return False

# 벽을 설치할 수 있는 모든 경우를 찾는 함수
def solution(count):
  global answer
  if count == 3:
    cnt = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check_S(i, j):          
            cnt += 1
    # 모든 선생이 감시가 불가능할 때
    if cnt == teacher:
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        count += 1
        solution(count)
        graph[i][j] = 'X'
        count -= 1

answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')