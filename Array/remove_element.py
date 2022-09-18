# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

sol = Solution()
nums = [3,2,3,2,3,2,3,2]
val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))
print(nums)


