# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        best_len = 0
        cur_len = 0
        start_idx = 0
        end_idx = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if nums[end_idx] != 0:
                    cur_len = self.find_max_len(nums, start_idx, end_idx)
                best_len = max(best_len, cur_len)
                start_idx = i+1
                end_idx = i+1
            else:
                end_idx = i
        print(start_idx, end_idx)
        if start_idx < len(nums) and end_idx < len(nums):
            cur_len = self.find_max_len(nums, start_idx, end_idx)
            best_len = max(best_len, cur_len)
        
        return best_len

    def find_max_len(self, nums, start_idx, last_idx):
        total_neg = 0
        len_nums = last_idx - start_idx + 1
        first_neg_idx = -1
        last_neg_idx = -1

        for i in range(start_idx, last_idx+1):
            if nums[i] < 0:
                total_neg += 1
                if first_neg_idx == -1 or i < first_neg_idx:
                    first_neg_idx = i
                if last_neg_idx == -1 or i > last_neg_idx:
                    last_neg_idx = i
        
        if total_neg %2 == 0:
            return len_nums
        else:
            return max(len_nums - (first_neg_idx - start_idx + 1), last_neg_idx - start_idx)

sol = Solution()
nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]
nums = [-1,-2,-3,0,1]
nums = [-1, 2]
nums = [-1, 2, -1, 1]
nums = [-1]
nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
nums = [-7,-10,-7,21,20,-12,-34,26,2]
nums = [0,0,0,0,0]
print(sol.getMaxLen(nums))