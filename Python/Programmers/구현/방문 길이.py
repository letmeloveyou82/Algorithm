def solution(dirs):
    visited = []
    x, y = 0, 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for op in dirs:
        if op == 'U':
            idx = 0
        elif op == 'D':
            idx = 1
        elif op == 'R':
            idx = 2
        else:
            idx = 3
        nx, ny = x+dx[idx], y+dy[idx]
        v_x, v_y = x+(dx[idx]/2), y+(dy[idx]/2)
        if -5<=nx<=5 and -5<=ny<=5:
            if [v_x, v_y] not in visited:
                visited.append([v_x, v_y])
            x = nx
            y = ny
    return len(visited)