n, m = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

one_color_box = []
one_color_box_count = 0
empty_box_count = 0
for i in range(n):
    if box[i].count(0) == m:
        empty_box_count += 1
    if box[i].count(0) == m-1:
        for color in range(m):
            if box[i][color] != 0 and color not in one_color_box:
                one_color_box.append(color)
                one_color_box_count += 1
                break
result = n-1-one_color_box_count-empty_box_count
print(0 if result < 0 else result)