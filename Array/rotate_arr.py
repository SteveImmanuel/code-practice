# https://leetcode.com/problems/rotate-array/
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #alt 1
        total_rotate = k % len(nums)
        temp = nums[-total_rotate:] + nums[:-total_rotate]
        for i in range(len(nums)):
            nums[i] = temp[i]
        
sol = Solution()
nums = [-1,-100,3,99]
sol.rotate(nums, 3)
print(nums)