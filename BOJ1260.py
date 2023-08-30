from collections import deque
def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1,n+1):
        if visited[i] == 0 and i in graph[v]:
            dfs(i)

def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)

    while(q):
        v = q.popleft()
        print(v, end=" ")
        for i in range(1,n+1):
            if visited[i] == 0 and i in graph[v]:
                q.append(i)
                visited[i] = 1


n,m,v = map(int,input().split())
visited = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)