class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mem = [[None for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == 0:
                    mem[i][j] = grid[i][j]
                else:
                    min_sum = float('inf')
                    for k in range(n):
                        if j == k:
                            continue
                        min_sum = min(min_sum, grid[i][j] + mem[i-1][k])
                    mem[i][j] = min_sum
        # for x in mem:
        #     print(x)
        return min(mem[-1])
                    