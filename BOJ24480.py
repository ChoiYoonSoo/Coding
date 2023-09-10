import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    global count
    visited[start] = count

    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

N, M, R = map(int,input().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
count = 1

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
      graph[i].sort(reverse=True)

dfs(R)
for i in visited[1:]:
    print(i)