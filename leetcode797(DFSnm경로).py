import sys
sys.setrecursionlimit(10**6)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [False] * (len(graph)+1)
        answer = []

        def dfs(x,lst):

            if x == len(graph)-1:
                answer.append(lst.copy())
                return

            if not graph[x]:
                if lst[-1] == len(graph)-1:
                    answer.append(lst.copy())
                return
            
            visited[x] = True

            for i in graph[x]:
                if not visited[i]:
                    dfs(i,lst + [i])

            visited[x] = False


        dfs(0,[0])
        return answer