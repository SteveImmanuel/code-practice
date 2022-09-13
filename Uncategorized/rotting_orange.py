# https://leetcode.com/problems/rotting-oranges/
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        visitation_mat = [[False for _ in range(n)] for _ in range(m)]

        total_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    total_fresh += 1

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while len(queue) > 0:
            i, j, minute = queue.pop(0)
            if i >= m or i < 0 or j >= n or j < 0 or visitation_mat[i][j]:
                continue
            
            visitation_mat[i][j] = True
            if grid[i][j] != 0:
                total_minute = minute
                if grid[i][j] == 1:
                    total_fresh -= 1
                for dir in dirs:
                    queue.append((i+dir[0], j+dir[1], total_minute+1))
            
        if total_fresh > 0:
            return -1
        return total_minute            

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
# grid = [[0,2]]
print(sol.orangesRotting(grid))
