class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefix_sum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                prefix_sum[i][j] = matrix[i][j]    
                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j-1]
                       
        for i in range(1, m):
            for j in range(n):
                prefix_sum[i][j] += prefix_sum[i-1][j]
                
        total = 0
        for i1 in range(m):
            for i2 in range(i1, m):
                
                occ = defaultdict(int)
                occ[0] = 1
                for j in range(n):
                    cur_sum = prefix_sum[i2][j]
                    if i1 > 0:
                        cur_sum -= prefix_sum[i1-1][j]
                    if cur_sum - target in occ:
                        total += occ[cur_sum - target]
                    
                    occ[cur_sum] += 1
        
        return total
                        
                        
                    
                    
                    
                    