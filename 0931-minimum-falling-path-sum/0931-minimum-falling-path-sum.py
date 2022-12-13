class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mem = [None] * n
        
        for i in range(n):
            if i != 0:
                next_mem = [None] * n
                
            for j in range(n):
                if i == 0:
                    mem[j] = matrix[i][j]
                else:
                    min_before = mem[j]
                    if j - 1 >= 0:
                        min_before = min(min_before, mem[j-1])
                    if j + 1 < n:
                        min_before = min(min_before, mem[j+1])
                    next_mem[j] = matrix[i][j] + min_before
            
            if i != 0:
                for i in range(n):
                    mem[i] = next_mem[i]
            # print(i, mem)
        
        return min(mem)
                    