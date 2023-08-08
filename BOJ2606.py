def dfs(virus, start):
    visited.append(start)

    for i in range(len(virus[start])):
        if virus[start][i] not in visited:
            dfs(virus, virus[start][i])

computer = int(input())
N = int(input())
virus = [[] * computer for i in range(computer+1)]
visited = []

for i in range(N):
    a,b = map(int,input().split())
    virus[a].append(b)
    virus[b].append(a)

dfs(virus, 1)
print(len(visited))