n, m = map(int, input().split())

s = [] # 출력할 숫자들을 받아주는 리스트
visited = [False] * (n+1) # 방문했는지 체크하는 리스트

def dfs():
    if len(s) == m: # 리스트 s안에 m개의 요소가 쌓인다면 출력
        print(*s) # 리스트 요소 한 줄에 출력
        return
    for i in range(1, n+1):
        if visited[i]: # 방문했을 경우 아래 코드 무시
            continue
        # 백트래킹
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()