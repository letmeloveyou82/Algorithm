import sys, heapq
input = sys.stdin.readline

N = int(input())
easy = [] # (level, problem_id)
hard = [] # (-level, -problem_id)
alive = {} # problem_id -> level (유효한 것만)

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(easy, (L, P))
    heapq.heappush(hard, (-L, -P))
    alive[P] = L

def clean_easy():
    # top이 alive와 안 맞으면 버림
    while easy:
        L, P = easy[0]
        if alive.get(P) == L:
            return
        heapq.heappop(easy)

def clean_hard():
    while hard:
        nL, nP = hard[0]
        if alive.get(-nP) == -nL:
            return
        heapq.heappop(hard)

M = int(input())
for _ in range(M):
    parts = input().split()
    cmd = parts[0]

    if cmd == "add":
        P, L = int(parts[1]), int(parts[2])
        alive[P] = L
        heapq.heappush(easy, (L, P))
        heapq.heappush(hard, (-L, -P))

    elif cmd == "solved":
        P = int(parts[1])
        # 존재하면 제거 표시(힙에서는 lazy)
        if P in alive:
            del alive[P]

    elif cmd == "recommend":
        x = int(parts[1])
        if x == 1:
            clean_hard()
            print(-hard[0][1])
        elif x == -1:
            clean_easy()
            print(easy[0][1])