def dfs(node, graph, visited):
    global cnt
    visited[node] = 1 # 방문처리
    cnt += 1
    for i in graph[node]:
        if visited[i] == 0: 
            dfs(i, graph, visited)
    return

def solution(n, wires):
    answer = 100
    for cut in range(n-1):
        graph = [[] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        result = []
        for i in range(n-1):
            if cut == i:
                continue
            graph[wires[i][0]].append(wires[i][1])
            graph[wires[i][1]].append(wires[i][0])

        for i in range(1, n+1):
            if visited[i] == 0: # 방문하지 않은 경우 탐색
                global cnt
                cnt = 0
                dfs(i, graph, visited)
                result.append(cnt)

        answer = min(answer, abs(result[0]-result[1]))
    return answer