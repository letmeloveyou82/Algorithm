T = int(input())
for test_case in range(1, T+1):
    result = 0
    tmp = list(input())
    memory = list(map(int, tmp))
    now_value = [0] * len(memory)

    for i in range(len(memory)):
        if now_value[i] != memory[i]:
            now_value[i:] = [memory[i]] * (len(memory)-i)
            result += 1
    print(f"#{test_case} {result}")