# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if arr[-1] < target:
                continue
            elif arr[-1] == target:
                return True
            else:
                idx = bisect.bisect_left(arr, target)
                if arr[idx] == target:
                    return True
        return False
                

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 30
sol = Solution()
print(sol.searchMatrix(matrix, target))