class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_row = m - 1
        total = 0
        for j in range(n):
            for i in range(start_row, -1, -1):
                if grid[i][j] >= 0:
                    start_row = i
                    total += m - i - 1
                    
                    break
                else:
                    if i == 0:
                        start_row = 0
                        total += m
        return total
            