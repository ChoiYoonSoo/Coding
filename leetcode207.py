from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited, finish = set(), set()
        
        for x,y in prerequisites:
            graph[x].append(y)

        def dfs(cur):
            if cur in visited:
                return True
            if cur in finish:
                return False

            finish.add(cur)

            for i in graph[cur]:
                if not dfs(i):
                    return False
            finish.remove(cur)
            visited.add(cur)

            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        
        return True