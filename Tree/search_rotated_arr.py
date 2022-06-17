# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_nums = nums + nums
        res = self.searchRec(new_nums, target, 0, None)
        if res >= 0 :
            return res % len(nums)
        return res

    def searchRec(self, nums, target, startIdx, last_pivot):
        if len(nums) == 0:
            return -1
        mid_idx = len(nums) // 2
        mid_val = nums[mid_idx]
        if target == mid_val:
            return mid_idx + startIdx
        else:
            if len(nums) == 1:
                return -1
            elif last_pivot is None:
                if target < mid_val:
                    return self.searchRec(nums[:mid_idx], target, startIdx, mid_val)
                else:
                    return self.searchRec(nums[mid_idx+1:], target, startIdx + mid_idx + 1, mid_val)
            else:
                if target > last_pivot > mid_val:
                    return self.searchRec(nums[:mid_idx], target, startIdx, mid_val)
                elif target > last_pivot and mid_val > last_pivot: # normal case
                    if target < mid_val:
                        return self.searchRec(nums[:mid_idx], target, startIdx, mid_val)
                    else:
                        return self.searchRec(nums[mid_idx+1:], target, startIdx + mid_idx + 1, mid_val)
                elif target < last_pivot and mid_val < last_pivot: # normal case
                    if target < mid_val:
                        return self.searchRec(nums[:mid_idx], target, startIdx, mid_val)
                    else:
                        return self.searchRec(nums[mid_idx+1:], target, startIdx + mid_idx + 1, mid_val)
                elif target < last_pivot < mid_val:
                    return self.searchRec(nums[mid_idx+1:], target, startIdx + mid_idx + 1, mid_val)






sol = Solution()
nums = [4,5,6,7,0,1,2]

nums = [i for i in range(10)]
for i in range(10):
    temp = nums[i:] + nums[:i]
    target = 8
    print(temp)
    print(sol.search(temp, target))