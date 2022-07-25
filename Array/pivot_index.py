# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = [None] * len(nums)
        cumm_sum = 0

        for i,num in enumerate(nums):
            cumm_sum += num
            res[i] = cumm_sum

        pivot_idx = 0
        left_sum = 0

        while pivot_idx < len(nums):
            left_sum = res[pivot_idx - 1] if pivot_idx > 0 else 0
            right_sum = res[-1] - res[pivot_idx]
            if left_sum == right_sum:
                return pivot_idx

            pivot_idx += 1

        return -1

sol = Solution()
nums = [1]
print(sol.pivotIndex(nums))