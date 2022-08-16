# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        outcome = []
        for _ in range(len(grid) + 1):
            outcome.append([None] * len(grid[0]))

        for i in range(len(outcome)):
            for j in range(len(outcome[i])):
                if i == 0:
                    outcome[i][j] = j
                else:
                    last_pos = outcome[i-1][j]
                    if last_pos == -1:
                        outcome[i][j] = -1
                    else:

                        if (last_pos == 0 and grid[i-1][last_pos] == -1) or (last_pos == len(grid[i-1]) - 1 and grid[i-1][last_pos] == 1):
                            outcome[i][j] = -1
                        elif (last_pos > 0 and grid[i-1][last_pos-1] == 1 and grid[i-1][last_pos] == -1) or (last_pos < len(grid[i-1]) - 1 and grid[i-1][last_pos] == 1 and grid[i-1][last_pos+1] == -1):
                            outcome[i][j] = -1
                        else:
                            outcome[i][j] = last_pos + grid[i-1][last_pos]

        return outcome[-1]
        
        # for i in range(len(res)):
        #     if res[i] != -1:



sol = Solution()
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# grid = [[-1]]
# grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(sol.findBall(grid))