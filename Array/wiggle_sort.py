# https://leetcode.com/problems/wiggle-sort-ii/
from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swap = True
        # while swap:
        #     smaller = True
        #     swap = False
        #     for i in range(len(nums) - 1):
        #         if not ((smaller and nums[i] < nums[i+1]) or (not smaller and nums[i] > nums[i+1])):
        #             print(i, nums[i], nums[i+1], nums, smaller)
        #             swap = True
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        #         smaller = not smaller
            # break

        sort_nums = sorted(nums)
        i = (len(sort_nums) // 2) - 1 + (len(sort_nums) % 2)
        j = len(sort_nums) - 1
        k = 0
        flag = True
        while k < len(nums):
            if flag:
                nums[k] = sort_nums[i]
                i -= 1
            else:
                nums[k] = sort_nums[j]
                j -= 1
            flag = not flag
            k += 1

sol = Solution()
nums = [1,3,2,2,3,1]
nums = [1,5,1,1,6,4]
nums = [5,5,5,4,4,4,4]
nums = [4,5,5,6]
sol.wiggleSort(nums)
print(nums)