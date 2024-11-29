def solution(mats, park):
    mats = sorted(mats, reverse = True)
    r, c = len(park), len(park[0])

    for l in mats:
        start_idx_set = set((i, j) for i in range(r-l+1) for j in range(c-l+1))
        for a, b in start_idx_set:
            ans = set()
            for i in range(a, a+l):
                for j in range(b, b+l):
                    ans.add(park[i][j])
            if ans == {'-1'}:
                return l
    return -1