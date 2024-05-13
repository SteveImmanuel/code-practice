class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = abs(grid[i][j] - 1)

        total = (2 ** (n - 1)) * m
        for j in range(1, n):
            count_1 = m
            for i in range(m):
                if grid[i][j] == 0:
                    count_1 -= 1
            mult = max(count_1, m - count_1)
            total += (2 ** (n - 1 - j)) * mult
        
        return total