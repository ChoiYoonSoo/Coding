from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    visited.append([a,b])

    while(queue):
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or [nx,ny] in visited or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                visited.append([nx,ny])
                queue.append([nx,ny])

N,M = map(int,input().split())
graph = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

bfs(0,0)
print(graph[N-1][M-1])