# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        cumm_sum = 0

        for i,num in enumerate(nums):
            cumm_sum += num
            res[i] = cumm_sum

        return res

sol = Solution()
nums = [3,1,2,10,1]
print(sol.runningSum(nums))