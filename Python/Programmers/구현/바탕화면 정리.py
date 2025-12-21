def solution(wallpaper):
    h = len(wallpaper)
    w = len(wallpaper[0])

    files = []
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == '#':
                files.append([i, j])

    min_x, min_y, max_x, max_y = h, w, 0, 0
    for x, y in files:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        
    return [min_x, min_y, max_x+1, max_y+1]