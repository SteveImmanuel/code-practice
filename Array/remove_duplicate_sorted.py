# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_num = nums[0]
        counter = 1
        total_duplicates = 0
        
        i = 1
        first_dup_idx = 1
        last_idx = len(nums) - 1
        while i <= last_idx: 
            if nums[i] == cur_num:
                if counter == 1:
                    first_dup_idx = i
                counter += 1
                i += 1
            else:
                if counter > 1:
                    total_duplicates += counter - 1
                    idx_diff = i - first_dup_idx
                    for j in range(i, len(nums)):
                        nums[j-idx_diff] = nums[j]

                    last_idx = last_idx - counter + 1
                    i = first_dup_idx

                cur_num = nums[i]
                i += 1
                counter = 1
        if counter != 1:
            total_duplicates += counter - 1

        return len(nums) - total_duplicates



sol = Solution()
nums = [0,0,0,0,0,0]
print(sol.removeDuplicates(nums))
print(nums)