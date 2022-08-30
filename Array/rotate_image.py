# https://leetcode.com/problems/rotate-image/

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while i < (n//2):
            j = i
            while j < (n - i - 1):
                first_idx = (i,j)
                second_idx = (j, n - i - 1)
                third_idx = (n - i - 1, n - j - 1)
                fourth_idx = (n - j - 1, i)

                temp = matrix[first_idx[0]][first_idx[1]]
                matrix[first_idx[0]][first_idx[1]] = matrix[fourth_idx[0]][fourth_idx[1]]
                matrix[fourth_idx[0]][fourth_idx[1]] = matrix[third_idx[0]][third_idx[1]]
                matrix[third_idx[0]][third_idx[1]] = matrix[second_idx[0]][second_idx[1]]
                matrix[second_idx[0]][second_idx[1]] = temp

                j += 1
            i += 1
        
        return matrix

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(sol.rotate(matrix))