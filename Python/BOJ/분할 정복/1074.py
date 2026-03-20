import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

answer = 0

while N > 0:
    half = 2 ** (N-1)
    area = half * half
    
    # 1사분면
    if r < half and c < half:
        pass

    # 2사분면
    elif r < half and c >= half:
        answer += area
        c -= half

    # 3사분면
    elif r >= half and c < half:
        answer += 2 * area
        r -= half

    # 4사분면
    else:
        answer += 3 * area
        r -= half
        c -= half

    N -= 1

print(answer)
