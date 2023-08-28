N = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
curv = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x,y,d,g = map(int,input().split())
    curv[x][y] = 1
    directions = [d]

    for _ in range(g):
        for i in range(len(directions)-1, -1, -1):
            directions.append((directions[i]+1) % 4)

    for i in range(len(directions)):
        x = x + dx[directions[i]]
        y = y + dy[directions[i]]
        curv[x][y] = 1

count = 0
for i in range(100):
    for j in range(100):
        if curv[i][j] and curv[i+1][j] and curv[i][j+1] and curv[i+1][j+1]:
            count += 1
print(count)