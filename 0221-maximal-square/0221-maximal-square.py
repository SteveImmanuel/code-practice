class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        mem = [[None for _ in range(m)] for _ in range(n)]
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    mem[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    min_sur_area = min(mem[i-1][j], mem[i][j-1], mem[i-1][j-1])
                    if matrix[i][j] == '1':
                        mem[i][j] = min_sur_area + 1
                    else:
                        mem[i][j] = 0
                max_area = max(max_area, mem[i][j])
            # print(mem[i])

        return max_area * max_area