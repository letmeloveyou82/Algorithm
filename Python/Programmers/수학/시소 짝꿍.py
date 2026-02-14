from collections import defaultdict

def solution(weights):
    cnt = defaultdict(int)
    ans = 0

    for w in weights:
        # 1:1
        ans += cnt[w]

        # 2:3 비율 (작은쪽/큰쪽 둘 다)
        if (w * 2) % 3 == 0:
            ans += cnt[(w * 2) // 3]   # other = 2/3 w
        if (w * 3) % 2 == 0:
            ans += cnt[(w * 3) // 2]   # other = 3/2 w

        # 1:2 비율 (둘 다)
        if w % 2 == 0:
            ans += cnt[w // 2]         # other = w/2
        ans += cnt[w * 2]              # other = 2w

        # 3:4 비율 (둘 다)
        if (w * 3) % 4 == 0:
            ans += cnt[(w * 3) // 4]   # other = 3/4 w
        if (w * 4) % 3 == 0:
            ans += cnt[(w * 4) // 3]   # other = 4/3 w

        cnt[w] += 1

    return ans
