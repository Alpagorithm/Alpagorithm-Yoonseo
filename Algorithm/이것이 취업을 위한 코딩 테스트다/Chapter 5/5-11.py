# N x M 크기의 직사각형 형태의 미로
# 동빈이의 위치는 (1,1) 미로의 출구는 (N, M)
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1
# 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하는 프로그램

from collections import deque

# 입력 N과 M
n, m = map(int, input().split())

# 2차원 리스트 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        print(graph[n-1][m-1])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))