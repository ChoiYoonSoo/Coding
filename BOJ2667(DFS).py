# 섬 크기 구하는 문제랑 비슷 dx,dy를 활용해야함
N = int(input())
graph = []
answer = []
count = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    graph.append(list(map(int,input().rstrip())))
    
def dfs(x,y):
    global count
    graph[x][y] = 0
    
    for i in range(4): # 상 하 좌 우 이동
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        
        if graph[nx][ny] == 1:
            count += 1
            dfs(nx,ny)

for i in range(N):
    for j in range(len(graph)):
        if graph[i][j] == 1:
            count += 1
            dfs(i,j)
            answer.append(count)
            count = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)