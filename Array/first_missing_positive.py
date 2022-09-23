# https://leetcode.com/problems/first-missing-positive/
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = min(nums)

        if min_num <= 0:
            min_num = -min_num + 1
            for i in range(len(nums)):
                nums[i] += min_num
        else:
            min_num = 0
        
        last_idx_exist = False
        for i in range(len(nums)):
            idx = abs(nums[i]) - min_num
            print(idx)
            if idx < 0 or idx > len(nums) - 1:
                if idx == len(nums):
                    last_idx_exist = True
                continue
            if nums[idx] > 0:
                nums[idx] *= -1
        
        print(nums)
        i = 1
        while i < len(nums) and nums[i] < 0:
            i += 1
        
        if i == len(nums) and last_idx_exist:
            i += 1
        return i

sol = Solution()
nums = [0,-1,2]
nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
nums = [1,2,0]
nums = [1,1,1,1,1,1]
nums = [2,2,2,2,2]
nums = [1,2]
nums = [1]
print(sol.firstMissingPositive(nums))        