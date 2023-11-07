# DFS 특정 정점에서 특정 정점으로 갈 수 있는지 확인
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [False] * (n)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        def dfs(x):
            visited[x] = True

            for i in graph[x]:
                if visited[i] == False:
                    dfs(i)
        
        dfs(source)
        
        if visited[destination] == False:
            return False
        else:
            return True