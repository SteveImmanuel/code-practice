# https://leetcode.com/problems/sort-the-matrix-diagonally/
from typing import List

class Solution:
    def get_diagonal_el(self, mat, start_row, start_col):
        i = start_row
        j = start_col
        nrow, ncol = len(mat), len(mat[0])

        while i < nrow and j < ncol:
            yield (i, j)
            i += 1
            j += 1

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for k in range(len(mat)):
            elms = []
            for i,j in  self.get_diagonal_el(mat, k, 0):
                elms.append(mat[i][j])
            elms.sort()
            for idx, (i,j) in enumerate(self.get_diagonal_el(mat, k, 0)):
                mat[i][j] = elms[idx]

        for k in range(1, len(mat[0])):
            elms = []
            for i,j in  self.get_diagonal_el(mat, 0, k):
                elms.append(mat[i][j])
            elms.sort()
            for idx, (i,j) in enumerate(self.get_diagonal_el(mat, 0, k)):
                mat[i][j] = elms[idx]
        
        return mat

sol = Solution()
# mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
print(sol.diagonalSort(mat))