# 섬 크기중 가장 큰 섬
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        answer = []
        global count
        count = 0

        def dfs(grid,x,y,dx,dy):
            global count
            grid[x][y] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                
                if grid[nx][ny] == 1:
                    count += 1
                    dfs(grid,nx,ny,dx,dy)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    dfs(grid,i,j,dx,dy)
                    answer.append(count)
                    count = 0
        
        m = 0
        for i in answer:
            if m < i:
                m = i
        return m