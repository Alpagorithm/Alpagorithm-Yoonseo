# N x M
# 0끼리 상하좌우 연결되어있으면 서로 연결되어 있는 것으로 간주
# 각 노드들의 특징 0또는 1

def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return 0

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return 1
    return 0


# 입력 N과 M
n, m = map(int, input().split())

# 2차원 리스트 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)


result = 0

for i in range(n):
    for j in range(m):
        result += dfs(i, j)

print(result)