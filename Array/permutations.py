# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i, num in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            rest_result = self.permute(rest)
            for item in rest_result:
                res.append([num] + item)
        return res

sol = Solution()
nums = [1,2,3,4]
print(len(sol.permute(nums)))