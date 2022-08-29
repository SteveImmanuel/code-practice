# https://leetcode.com/problems/number-of-islands/

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitation_map = []
        for _ in range(len(grid)):
            visitation_map.append([False] * len(grid[0]))
        total_island = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visitation_map[i][j]:
                    total_island += 1
                    self.DFS(i,j,grid,visitation_map)
        return total_island

    def DFS(self, current_row, current_col, grid, visitation_map):
        visitation_map[current_row][current_col] = True
        if current_row > 0 and grid[current_row-1][current_col] == '1' and not visitation_map[current_row-1][current_col]:
            self.DFS(current_row-1, current_col, grid, visitation_map)
        if current_row < len(grid) - 1 and grid[current_row+1][current_col] == '1' and not visitation_map[current_row+1][current_col]:
            self.DFS(current_row+1, current_col, grid, visitation_map)
        if current_col > 0 and grid[current_row][current_col-1] == '1' and not visitation_map[current_row][current_col-1]:
            self.DFS(current_row, current_col-1, grid, visitation_map)
        if current_col < len(grid[0]) - 1 and grid[current_row][current_col+1] == '1' and not visitation_map[current_row][current_col+1]:
            self.DFS(current_row, current_col+1, grid, visitation_map)


sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))