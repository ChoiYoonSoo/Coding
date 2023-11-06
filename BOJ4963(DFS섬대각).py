# 섬 갯수 문제인데 대각선까지 포함
import sys
sys.setrecursionlimit(5000)

dx = [1, -1, 0, 0, 1, -1, 1, -1] # 그래프의 탐색 방향 대각선 포함
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def dfs(x, y):
    global count
    graph[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        
        if graph[nx][ny] == 1:
            dfs(nx,ny)


answer = []
while True:
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    answer.append(count)

for i in answer:
    print(i)