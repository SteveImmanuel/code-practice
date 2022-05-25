# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_streak = 1
                curr_num = num + 1

                while curr_num in num_set:
                    curr_num += 1
                    curr_streak += 1

                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
        
sol = Solution()
x = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(x))
    