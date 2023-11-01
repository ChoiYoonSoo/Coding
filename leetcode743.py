from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        time = [99999] * (n+1)

        for u,v,w in times:
            graph[u].append([v,w])

        def bfs(x):
            q = deque()
            q.append(x)
            time[x] = 0
            
            while q:
                node = q.popleft()
                for a,b in graph[node]:
                    if time[node] + b < time[a]:
                        time[a] = time[node] + b
                        q.append(a)

            if max(time[1:]) < 99999:
                return max(time[1:])
            else:
                return -1
        
        return bfs(k)