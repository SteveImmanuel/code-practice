class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [sum(x) for x in grid]
        
        ones_col = []
        for j in range(n):
            total = 0
            for i in range(m):
                if grid[i][j] == 1:
                    total += 1
            ones_col.append(total)
        
        res = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2 * (ones_row[i] + ones_col[j]) - n - m
        return res