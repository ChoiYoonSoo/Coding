import sys
sys.setrecursionlimit(10 ** 6)

count = 1
def dfs(graph,start,visited):
    global count
    visited[start] = count
    
    for node in graph[start]:
        if visited[node] == 0:
            count += 1
            dfs(graph,node,visited)

V,E,R = map(int,input().split())

graph = [[] for x in range(V+1)]
visited = [0] * (V+1)

for i in range(E):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(V+1):
    graph[i].sort()

dfs(graph,R,visited)

for i in range(V+1):
    if i != 0:
        print(visited[i])