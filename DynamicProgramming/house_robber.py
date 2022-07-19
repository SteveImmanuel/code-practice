# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_mem = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp_mem[i] = (nums[i], 0)
            else:
                dp_mem[i] = (nums[i] + dp_mem[i-1][1], max(dp_mem[i-1][0], dp_mem[i-1][1]))
        return max(dp_mem[-1])


sol = Solution()
nums = [2,1,1,2]
print(sol.rob(nums))