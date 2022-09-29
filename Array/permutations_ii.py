# https://leetcode.com/problems/permutations-ii/
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        num_set = set()
        res = []
        for i, num in enumerate(nums):
            if num not in num_set:
                rest = nums[:i] + nums[i+1:]
                rest_result = self.permuteUnique(rest)
                for item in rest_result:
                    res.append([num] + item)
                num_set.add(num)
        return res

sol = Solution()
nums = [2, 2,3,4]
print(sol.permuteUnique(nums))
print(len(sol.permuteUnique(nums)))