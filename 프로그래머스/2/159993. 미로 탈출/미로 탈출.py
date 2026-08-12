from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dy = [-1, 1, 0, 0]  # 상, 하 이동
    dx = [0, 0, -1, 1]  # 좌, 우 이동

    # visited[y][x][레버상태] : 레버상태 0=안당김, 1=당김
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

    # 시작 지점 S 좌표 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                s = (i, j)

    # 큐에 (y, x, 레버여부, 여기까지 걸린 시간) 넣고 시작
    queue = deque([(s[0], s[1], False, 0)])
    visited[s[0]][s[1]][0] = True

    while queue:
        q = queue.popleft()

        for i in range(4):
            ny = dy[i] + q[0]
            nx = dx[i] + q[1]

            # 미로 범위를 벗어나면 스킵 (여기가 빠져있던 부분)
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            cell = maps[ny][nx]

            # 벽이면 못 지나감
            if cell == "X":
                continue

            # 같은 레버 상태로 이미 방문한 칸이면 스킵
            if visited[ny][nx][q[2]]:
                continue

            if cell in "OS":
                # 통로/시작점: 레버 상태 그대로 유지하며 이동
                queue.append((ny, nx, q[2], q[3] + 1))
                visited[ny][nx][q[2]] = True
            elif cell == "L":
                # 레버 칸: 레버 당긴 상태(True)로 전환해서 이동
                queue.append((ny, nx, True, q[3] + 1))
                visited[ny][nx][1] = True
            elif cell == "E":
                if q[2] == 1:
                    # 레버를 당긴 상태로 출구 도착 -> 진짜 탈출
                    return q[3] + 1
                else:
                    # 레버 안 당긴 상태로 출구는 그냥 지나가기만 함
                    queue.append((ny, nx, False, q[3] + 1))
                    visited[ny][nx][0] = True

    return -1  # 큐가 다 빌 때까지 탈출 못하면 -1