class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for item in matrix:
            arr += item
            
        l, h = 0, len(arr) - 1
        while l <= h:
            m = (l + h) // 2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                h = m - 1
            else:
                l = m + 1
        return False