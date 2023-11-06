for tc_num in range(1, 11):
    dump_num = int(input())
    box_height = list(map(int, input().split()))
    result = 0
    for i in range(dump_num):
        max_value = max(box_height)
        min_value = min(box_height)
        if max_value - min_value <= 1:
            break
        max_idx = box_height.index(max_value)
        min_idx = box_height.index(min_value)
        box_height[min_idx] += 1
        box_height[max_idx] -= 1
    result = max(box_height) - min(box_height)
    print(f"#{tc_num} {result}")
