# https://leetcode.com/problems/subsets/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(1, len(nums) + 1):
            result += self.subsetsRec(nums, i)
        return result

    def subsetsRec(self, nums, length):
        if length == 1:
            return [[el] for el in nums]
        else:
            result = []

            for i in range(len(nums) - length + 1):
                anchor = nums[i:i+1]
                rest = nums[i+1:]

                subset_rest = self.subsetsRec(rest, length - 1)
                for subs in subset_rest:
                    result.append(anchor + subs)

            return result



sol = Solution()
nums = [1,2,3,4]
print(sol.subsets(nums))