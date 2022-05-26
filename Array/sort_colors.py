# https://leetcode.com/problems/sort-colors/submissions/
from collections import Counter
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        occ = Counter(nums)
        
        cur_idx = 0
        for i in range(3):
            count = occ[i]
            
            while count > 0:
                nums[cur_idx] = i
                cur_idx += 1
                count -= 1

sol = Solution()
x = [2,0,2,1,1,0]
print(sol.sortColors(x))