# https://leetcode.com/problems/combination-sum-iv/
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {}
        total = self.traverse(0, target, nums, mem)
        return total

    def traverse(self, current_total, target, nums, mem):
        if current_total > target:
            return 0
        elif current_total == target:
            return 1
        else:
            possible = 0
            for num in nums:
                if current_total+num not in mem:
                    mem[current_total+num] = self.traverse(current_total+num, target, nums, mem)
                possible += mem[current_total+num]
            return possible

sol = Solution()
nums = [4,2,1]
target = 32
print(sol.combinationSum4(nums, target))