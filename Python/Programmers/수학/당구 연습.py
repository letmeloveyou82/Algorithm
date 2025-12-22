def solution(m, n, startX, startY, balls):
    answer = []

    for targetX, targetY in balls:
        candidates = []

        # 1. 위쪽 벽
        # 같은 x이고, 목표가 위에 있으면 벽 맞기 전에 직선으로 먼저 맞음 → 제외
        if not (startX == targetX and startY < targetY):
            candidates.append(
                (startX - targetX) ** 2 +
                (n - startY + n - targetY) ** 2
            )

        # 2. 오른쪽 벽
        if not (startY == targetY and startX < targetX):
            candidates.append(
                (m - startX + m - targetX) ** 2 +
                (startY - targetY) ** 2
            )

        # 3. 아래쪽 벽
        if not (startX == targetX and startY > targetY):
            candidates.append(
                (startX - targetX) ** 2 +
                (startY + targetY) ** 2
            )

        # 4. 왼쪽 벽
        if not (startY == targetY and startX > targetX):
            candidates.append(
                (startX + targetX) ** 2 +
                (startY - targetY) ** 2
            )

        answer.append(min(candidates))

    return answer
