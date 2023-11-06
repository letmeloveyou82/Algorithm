for tc_num in range(1, 11):
    N = int(input()) # 건물의 개수
    building_height = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        if building_height[i] == max(building_height[i-2], building_height[i-1], building_height[i], building_height[i+1], building_height[i+2]):
            result += building_height[i] - max(building_height[i-2], building_height[i-1], building_height[i+1], building_height[i+2])
    print(f"#{tc_num} {result}")