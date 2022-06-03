# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

class Solution:
    def combine(self, arr1, arr2):
        res = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1

        while j < len(arr2):
            res.append(arr2[j])
            j += 1

        return res

    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        
        head = arr[:mid]
        tail = arr[mid:]

        return self.combine(self.merge_sort(head), self.merge_sort(tail))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = self.merge_sort(nums)
        return sorted_nums[-k]

sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(sol.findKthLargest(nums, k))