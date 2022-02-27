# https://leetcode.com/problems/unique-paths-ii/

from typing import List


# 01
# 00

# 0000
# 0101
# 0000

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memory = []
        for i in range(len(obstacleGrid)):
            memory.append([None] * len(obstacleGrid[i]))

        memory[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(len(memory)):
            for j in range(len(memory[i])):
                if i == 0 and j == 0:
                    continue

                if obstacleGrid[i][j] == 1:
                    memory[i][j] = 0
                    continue

                from_up = 0
                from_left = 0

                if i > 0:
                    from_up = memory[i-1][j]
                
                if j > 0:
                    from_left = memory[i][j-1]

                memory[i][j] = from_up + from_left


sol = Solution()
grid = [[0,1,0],[1,0,0],[0,0,0]]
print(sol.uniquePathsWithObstacles(grid))