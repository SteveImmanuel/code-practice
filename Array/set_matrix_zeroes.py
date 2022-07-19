# https://leetcode.com/problems/set-matrix-zeroes/
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_exist = False
        zero_col_exist = False
        if 0 in matrix[0]:
            zero_row_exist = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_col_exist = True

        # zero_indices = []
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    # zero_indices.append((i, j))
        # unique_rows = set(map(lambda x: x[0], zero_indices))
        # unique_cols = set(map(lambda x: x[1], zero_indices))
        # for a in matrix:
        #     print(a)
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        

        # print(zero_col_exist, zero_row_exist)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i == 0 and zero_row_exist) or (j == 0 and zero_col_exist):
                    matrix[i][j] = 0

        
        


sol = Solution()
matrix = [[1,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
for a in matrix:
    print(a)