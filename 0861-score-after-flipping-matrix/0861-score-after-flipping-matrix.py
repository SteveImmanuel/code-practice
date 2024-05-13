class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = abs(grid[i][j] - 1)

        for j in range(n):
            count_1 = m
            for i in range(m):
                if grid[i][j] == 0:
                    count_1 -= 1
            count_0 = m - count_1
            if count_1 < count_0:
                for i in range(m):
                    grid[i][j] = abs(grid[i][j] - 1)
        
        total = 0
        for i in range(m):
            num = ''.join(map(str, grid[i]))
            num = int('0b' + num, 2)
            total += num
        return total