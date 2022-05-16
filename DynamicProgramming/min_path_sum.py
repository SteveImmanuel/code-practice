# https://leetcode.com/problems/minimum-path-sum/
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memory = []
        for i in range(len(grid)):
            memory.append([None] * len(grid[i]))

        for i in range(len(memory)):
            for j in range(len(memory[i])):       
                if i == 0 and j == 0:
                    memory[i][j] = grid[i][j]
                elif i == 0:
                    memory[i][j] = grid[i][j] + memory[i][j-1]
                elif j == 0:
                    memory[i][j] = grid[i][j] + memory[i-1][j]
                else:
                    memory[i][j] = grid[i][j] + min(memory[i-1][j], memory[i][j-1])

        return memory[-1][-1]

sol = Solution()
grid = [[1,2,3],[4,5,6]]
print(sol.minPathSum(grid))