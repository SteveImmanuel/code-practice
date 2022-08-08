# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [None] * len(nums)
        for i in range(len(nums)):
            if i==0:
                mem[i] = 1
            else:
                max_len = 1
                for j in range(i):
                    if nums[i] > nums[j] and mem[j] + 1 > max_len:
                        max_len = mem[j] + 1
                mem[i] = max_len
        return max(mem)

sol = Solution()
nums = [7,7,7,7,7,7,7]
print(sol.lengthOfLIS(nums))