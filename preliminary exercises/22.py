rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

visited = [[False] * cols for i in range(rows)]

dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]

def dfs(i, j):

    visited[i][j] = True

    for dr, dc in dir:
        nr = i + dr
        nc = j + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if matrix[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)

count = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1 and not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)