class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)
        sum = 0
        if dim % 2 != 0:
            sum -= mat[dim//2][dim//2]
        
        for i in range(dim):
            sum += mat[i][i] + mat[i][dim - 1 - i]
        
        return sum